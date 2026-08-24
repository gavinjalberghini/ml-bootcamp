#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Lint commit subjects against the mentorship Conventional Commit rule.

Usage:
    python3 scripts/lint_commits.py --base <sha> --head <sha>
    python3 scripts/lint_commits.py --subject 'feat(pa-knn): implement leave-one-out'
    python3 scripts/lint_commits.py --self-test
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys

TYPES = ('feat', 'fix', 'docs', 'chore', 'test', 'refactor', 'style')
SCOPES = (
    'git',
    'uv',
    'taskfile',
    'pa-knn',
    'pa-scaled',
    'pa-metrics',
    'pa-selection',
    'pa-ensemble',
    'pa-gpu',
    'pa-online',
    'ra-types',
    'ra-scaling',
    'ra-selection',
    'ra-ensembles',
    'ra-streaming',
    'ra-hardware',
    'ra-drift',
    'ra-imbalance',
    'ra-cost',
    'lr-jetson',
    'lr-slam',
    'repo',
    'data',
    'ci',
)
SUBJECT_RE = re.compile(
    rf'^(?:{"|".join(TYPES)})\((?:{"|".join(SCOPES)})\): [a-z0-9].{{0,71}}$'
)
MAX_LEN = 72
CONVENTION_FILE = 'scripts/lint_commits.py'


def is_skipped(subject: str) -> bool:
    return subject.startswith('Merge ') or subject.startswith('Revert "')


def check_subject(subject: str) -> str | None:
    """Return an error string, or None if the subject is allowed."""
    if is_skipped(subject):
        return None
    if len(subject) > MAX_LEN:
        return f'first line is {len(subject)} characters (max {MAX_LEN})'
    if not SUBJECT_RE.match(subject):
        return (
            'expected type(scope): description with a known scope and a '
            'lowercase description start; see .github/commit-convention.md'
        )
    return None


def git(*args: str) -> str:
    result = subprocess.run(
        ['git', *args],
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr or f'git {" ".join(args)} failed')
    return result.stdout


def subjects_between(base: str, head: str) -> list[tuple[str, str]]:
    raw = git('log', '--format=%H\t%s', f'{base}..{head}')
    rows = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        sha, subject = line.split('\t', 1)
        rows.append((sha, subject))
    return rows


def first_convention_commit(base: str, head: str) -> str | None:
    raw = git(
        'log',
        '--diff-filter=A',
        '--format=%H',
        f'{base}..{head}',
        '--',
        CONVENTION_FILE,
    )
    shas = [line.strip() for line in raw.splitlines() if line.strip()]
    return shas[-1] if shas else None


def lint_range(base: str, head: str) -> int:
    rows = subjects_between(base, head)
    start = first_convention_commit(base, head)
    if start:
        shas = [sha for sha, _ in rows]
        if start in shas:
            keep = shas[: shas.index(start) + 1]
            rows = [(sha, subject) for sha, subject in rows if sha in keep]

    failed = 0
    for sha, subject in rows:
        error = check_subject(subject)
        if error:
            failed += 1
            print(f'{sha[:12]}  {subject}')
            print(f'  {error}')
    if failed:
        print(
            f'\n{failed} commit(s) do not match type(scope): description. '
            'See .github/commit-convention.md.'
        )
        return 1
    print(f'ok: {len(rows)} commit(s) match type(scope): description')
    return 0


def self_test() -> int:
    cases = [
        ('feat(pa-knn): implement leave-one-out kNN', None),
        ('feat(taskfile): add hello and echo-vars tasks', None),
        ('docs(git): fill in the learning log', None),
        ('fix(pa-scaled): fit z-score on the pool only', None),
        ('Merge branch \'git/setup\'', None),
        ('updated knn', 'expected'),
        ('feat: implement knn', 'expected'),
        ('feat(PA1): implement knn', 'expected'),
        ('feat(pa-knn): Implement leave-one-out', 'expected'),
        ('feat(unknown): do a thing', 'expected'),
        ('feat(pa-knn): ' + ('x' * 70), 'first line'),
    ]
    failed = 0
    for subject, expect in cases:
        error = check_subject(subject)
        ok = error is None if expect is None else (error is not None and expect in error)
        if not ok:
            failed += 1
            print(f'FAIL {subject!r} -> {error!r}')
    if failed:
        return 1
    print(f'ok: {len(cases)} self-test cases')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description='Lint conventional commit subjects')
    parser.add_argument('--base', help='exclusive start SHA (PR base)')
    parser.add_argument('--head', help='inclusive end SHA (PR head)')
    parser.add_argument('--subject', help='check one subject and exit')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.subject is not None:
        error = check_subject(args.subject)
        if error:
            print(error)
            return 1
        print('ok')
        return 0
    if not args.base or not args.head:
        parser.error('provide --base and --head, or --subject, or --self-test')
    return lint_range(args.base, args.head)


if __name__ == '__main__':
    sys.exit(main())

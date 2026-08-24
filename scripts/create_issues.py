#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Create GitHub issues from issues/*.md using the gh CLI.

Idempotent: skips a title that already exists (open or closed).

Usage (from the repo root, after `gh auth login`):
    python3 scripts/create_issues.py --repo owner/name
    python3 scripts/create_issues.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys


def parse_issue(path: pathlib.Path):
    text = path.read_text()
    lines = text.splitlines()
    if not lines or not lines[0].startswith('# '):
        raise SystemExit(f'{path} must start with a "# title" line')
    title = lines[0][2:].strip()
    body = '\n'.join(lines[1:]).lstrip('\n')
    if not body.endswith('\n'):
        body += '\n'
    return title, body


def existing_titles(repo: str | None) -> set[str]:
    cmd = ['gh', 'issue', 'list', '--state', 'all', '--limit', '200', '--json', 'title']
    if repo:
        cmd.extend(['--repo', repo])
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        raise SystemExit(result.returncode)
    rows = json.loads(result.stdout or '[]')
    return {row['title'] for row in rows}


def run(repo: str | None = None, dry_run: bool = False) -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    files = sorted((root / 'issues').glob('*.md'))
    if not files:
        raise SystemExit('no issue files found in issues/')

    have = set() if dry_run else existing_titles(repo)
    created = 0
    for path in files:
        title, body = parse_issue(path)
        if title in have:
            print(f'{path.name}: skip (exists) {title}')
            continue
        print(f'{path.name}: {title}')
        if dry_run:
            created += 1
            continue
        cmd = ['gh', 'issue', 'create', '--title', title, '--body', body]
        if repo:
            cmd.extend(['--repo', repo])
        result = subprocess.run(cmd, cwd=root, text=True, capture_output=True)
        if result.returncode != 0:
            sys.stderr.write(result.stderr)
            raise SystemExit(result.returncode)
        print(result.stdout.strip())
        created += 1
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description='Create GitHub issues from issues/*.md')
    parser.add_argument('--repo', help='owner/name (defaults to the current gh repo)')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    run(repo=args.repo, dry_run=args.dry_run)
    return 0


if __name__ == '__main__':
    sys.exit(main())

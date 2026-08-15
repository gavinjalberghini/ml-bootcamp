#!/usr/bin/env python3
"""Create GitHub issues from issues/*.md using the gh CLI.

Usage (from the repo root, after `gh auth login`):
    python3 scripts/create_issues.py
    python3 scripts/create_issues.py --repo owner/name
"""
import argparse
import pathlib
import subprocess
import sys


def parse_issue(path):
    text = path.read_text()
    lines = text.splitlines()
    if not lines or not lines[0].startswith('# '):
        raise SystemExit(f'{path} must start with a "# title" line')
    title = lines[0][2:].strip()
    body = '\n'.join(lines[1:]).lstrip('\n')
    if not body.endswith('\n'):
        body += '\n'
    return title, body


def main():
    parser = argparse.ArgumentParser(description='Create GitHub issues from issues/*.md')
    parser.add_argument('--repo', help='owner/name (defaults to the current gh repo)')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parents[1]
    files = sorted((root / 'issues').glob('*.md'))
    if not files:
        raise SystemExit('no issue files found in issues/')

    for path in files:
        title, body = parse_issue(path)
        cmd = ['gh', 'issue', 'create', '--title', title, '--body', body]
        if args.repo:
            cmd.extend(['--repo', args.repo])
        print(f'{path.name}: {title}')
        if args.dry_run:
            continue
        result = subprocess.run(cmd, cwd=root, text=True, capture_output=True)
        if result.returncode != 0:
            sys.stderr.write(result.stderr)
            raise SystemExit(result.returncode)
        print(result.stdout.strip())


if __name__ == '__main__':
    main()

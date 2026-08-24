#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Instantiate a student repo in a mentor-owned GitHub organization.

Creates `org/ml-bootcamp-<student>` from this source tree, invites the
student with Write (not Admin), opens the assignment issues, and applies
per-repo main-branch protection. Run once per mentee as an org owner:

    python3 scripts/deploy_student.py --org my-org --student jane
    python3 scripts/deploy_student.py --org my-org --student jane --dry-run

Does not take a student PAT. Uses your `gh auth login` session.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from create_issues import run as create_issues
from gh_api import gh_json, run_gh
from setup_github_rules import run as apply_repo_rules

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PREFIX = 'ml-bootcamp'
LOGIN_RE = re.compile(r'^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$')


def die(message: str) -> None:
    raise SystemExit(message)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True)
    if check and result.returncode != 0:
        die(result.stderr.strip() or result.stdout.strip() or f'git {" ".join(args)} failed')
    return result


def repo_name_for(student: str, name: str | None) -> str:
    if name:
        return name
    return f'{DEFAULT_PREFIX}-{student.lower()}'


def validate_login(login: str) -> str:
    if not LOGIN_RE.match(login):
        die(f'invalid GitHub login {login!r}')
    return login


def resolve_ref(ref: str | None) -> str:
    if ref:
        git('rev-parse', '--verify', ref)
        return ref
    for candidate in ('main', 'origin/main'):
        probed = git('rev-parse', '--verify', candidate, check=False)
        if probed.returncode == 0:
            return candidate
    return 'HEAD'


def repo_exists(owner_repo: str) -> bool:
    result = run_gh(['repo', 'view', owner_repo, '--json', 'nameWithOwner'])
    return result.returncode == 0


def create_repo(owner_repo: str, visibility: str, description: str, dry_run: bool) -> str:
    if repo_exists(owner_repo):
        return f'exists {owner_repo}'
    cmd = [
        'repo',
        'create',
        owner_repo,
        f'--{visibility}',
        '--disable-wiki',
        '--description',
        description,
    ]
    if dry_run:
        return f'would create {owner_repo} ({visibility})'
    result = run_gh(cmd)
    if result.returncode != 0:
        die(result.stderr or result.stdout or f'failed to create {owner_repo}')
    return f'created {owner_repo}'


def push_source(owner_repo: str, ref: str, force: bool, dry_run: bool) -> str:
    dest = f'{ref}:refs/heads/main'
    if dry_run:
        return f'would git push {ref} -> {owner_repo} main' + (' (force)' if force else '')
    token_proc = run_gh(['auth', 'token'])
    token = token_proc.stdout.strip()
    if token_proc.returncode != 0 or not token:
        die('gh auth token failed; run gh auth login as an org owner')
    url = f'https://x-access-token:{token}@github.com/{owner_repo}.git'
    cmd = ['push']
    if force:
        cmd.append('--force')
    cmd.extend([url, dest])
    result = git(*cmd, check=False)
    if result.returncode != 0:
        die(
            (result.stderr or result.stdout).strip()
            + '\npush failed. If main already has student work, do not --force-source. '
            'If this is a brand-new repo, check org rulesets / your owner access.'
        )
    return f'pushed {ref} to {owner_repo} main'


def invite_student(owner_repo: str, student: str, dry_run: bool) -> str:
    if dry_run:
        return f'would invite {student} to {owner_repo} with Write'
    data, err = gh_json(
        ['-X', 'PUT', f'repos/{owner_repo}/collaborators/{student}', '-f', 'permission=push']
    )
    if err:
        die(
            f'failed to invite {student} ({err}). '
            'If the org forbids outside collaborators, add them as an org member '
            'first (`--org-member`) or invite them in the GitHub UI.'
        )
    status = 'invited'
    if isinstance(data, dict) and data.get('permissions', {}).get('push'):
        status = 'already had Write' if not data.get('html_url') else 'invited'
    return f'{status} {student} on {owner_repo} (Write)'


def invite_org_member(org: str, student: str, dry_run: bool) -> str:
    member, _ = gh_json([f'orgs/{org}/members/{student}'])
    if member is not None and not isinstance(member, str):
        return f'{student} is already an org member'
    user, err = gh_json([f'users/{student}'])
    if err or not isinstance(user, dict) or 'id' not in user:
        die(f'cannot resolve GitHub user {student}: {err or user}')
    if dry_run:
        return f'would invite {student} to org {org} as a member'
    _, invite_err = gh_json(
        ['-X', 'POST', f'orgs/{org}/invitations', '--input', '-'],
        {'invitee_id': user['id'], 'role': 'direct_member'},
    )
    if invite_err:
        if 'already' in invite_err.lower() or '422' in invite_err:
            return f'org invite for {student}: {invite_err}'
        die(f'failed to invite {student} to org {org}: {invite_err}')
    return f'invited {student} to org {org}'


def main() -> int:
    parser = argparse.ArgumentParser(description='Create a student repo in a mentor org')
    parser.add_argument('--org', default=os.environ.get('ML_BOOTCAMP_ORG'), help='org login (or $ML_BOOTCAMP_ORG)')
    parser.add_argument('--student', required=True, help='student GitHub login')
    parser.add_argument('--name', help=f'repo name (default: {DEFAULT_PREFIX}-<student>)')
    parser.add_argument('--ref', help='git ref to push as main (default: main, else HEAD)')
    parser.add_argument('--public', action='store_true', help='create a public repo (default private)')
    parser.add_argument('--org-member', action='store_true', help='also invite the student to the org')
    parser.add_argument('--force-source', action='store_true', help='force-push main (destroys student commits)')
    parser.add_argument('--skip-push', action='store_true')
    parser.add_argument('--skip-invite', action='store_true')
    parser.add_argument('--skip-issues', action='store_true')
    parser.add_argument('--skip-rules', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    if not args.org:
        die('pass --org or set ML_BOOTCAMP_ORG')

    student = validate_login(args.student)
    name = repo_name_for(student, args.name)
    owner_repo = f'{args.org}/{name}'
    visibility = 'public' if args.public else 'private'
    ref = resolve_ref(args.ref)
    description = f'ML bootcamp classification sequence for {student}'

    print(f'source: {ROOT}')
    print(f'ref:    {ref}')
    print(f'dest:   {owner_repo} ({visibility})')
    print(f'student Write: {student}')
    print(create_repo(owner_repo, visibility, description, args.dry_run))
    if not args.skip_push:
        print(push_source(owner_repo, ref, args.force_source, args.dry_run))
    if args.org_member:
        print(invite_org_member(args.org, student, args.dry_run))
    if not args.skip_invite:
        print(invite_student(owner_repo, student, args.dry_run))
    if not args.skip_issues:
        created = create_issues(repo=owner_repo, dry_run=args.dry_run)
        print(f'issues: {created} created or already present')
    if not args.skip_rules:
        for line in apply_repo_rules(repo=owner_repo, dry_run=args.dry_run):
            print(line)
    print()
    print(f'Student URL: https://github.com/{owner_repo}')
    print('Ask them to accept the invite, then start at the [git] issue.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

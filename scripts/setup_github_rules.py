#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Protect main: no direct push; pull requests need one approving review.

Uses the GitHub CLI (`gh auth login` first). Idempotent: updates the
existing `protect-main` ruleset when it is already there, and also applies
classic branch protection with `enforce_admins` so the repo owner cannot
bypass the rule.

Usage (from the repo root):
    python3 scripts/setup_github_rules.py
    python3 scripts/setup_github_rules.py --repo owner/name
    python3 scripts/setup_github_rules.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys

RULESET_NAME = 'protect-main'

PULL_REQUEST_RULE = {
    'type': 'pull_request',
    'parameters': {
        'required_approving_review_count': 1,
        'dismiss_stale_reviews_on_push': True,
        'require_code_owner_review': False,
        'require_last_push_approval': False,
        'required_review_thread_resolution': False,
        'allowed_merge_methods': ['merge', 'squash', 'rebase'],
    },
}

RULESET_BODY = {
    'name': RULESET_NAME,
    'target': 'branch',
    'enforcement': 'active',
    'bypass_actors': [],
    'conditions': {
        'ref_name': {
            'include': ['refs/heads/main'],
            'exclude': [],
        }
    },
    'rules': [
        {'type': 'deletion'},
        {'type': 'non_fast_forward'},
        PULL_REQUEST_RULE,
    ],
}

CLASSIC_PROTECTION = {
    'required_status_checks': None,
    'enforce_admins': True,
    'required_pull_request_reviews': {
        'dismiss_stale_reviews': True,
        'require_code_owner_reviews': False,
        'required_approving_review_count': 1,
        'require_last_push_approval': False,
    },
    'restrictions': None,
    'allow_force_pushes': False,
    'allow_deletions': False,
    'block_creations': False,
    'required_conversation_resolution': False,
    'lock_branch': False,
    'allow_fork_syncing': True,
}


def gh_json(args: list[str], input_obj=None):
    cmd = ['gh', 'api', *args]
    payload = None if input_obj is None else json.dumps(input_obj)
    result = subprocess.run(cmd, text=True, capture_output=True, input=payload)
    if result.returncode != 0:
        return None, result.stderr.strip() or result.stdout.strip()
    text = result.stdout.strip()
    if not text:
        return {}, None
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return text, None


def repo_info(repo: str | None):
    cmd = ['gh', 'repo', 'view']
    if repo:
        cmd.append(repo)
    cmd.extend(['--json', 'nameWithOwner,defaultBranchRef'])
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.returncode != 0:
        raise SystemExit(result.stderr or 'gh repo view failed; run gh auth login')
    data = json.loads(result.stdout)
    owner_repo = data['nameWithOwner']
    default_branch = data.get('defaultBranchRef', {}).get('name') or 'main'
    return owner_repo, default_branch


def find_ruleset_id(owner_repo: str):
    data, err = gh_json(['repos/' + owner_repo + '/rulesets'])
    if err:
        return None, err
    if not isinstance(data, list):
        return None, 'unexpected ruleset list'
    for item in data:
        if item.get('name') == RULESET_NAME:
            return item.get('id'), None
    return None, None


def apply_ruleset(owner_repo: str, dry_run: bool) -> str:
    body = json.loads(json.dumps(RULESET_BODY))
    existing, err = find_ruleset_id(owner_repo)
    if err and '404' in err:
        return f'skip ruleset ({err})'
    if err:
        return f'skip ruleset ({err})'
    path = f'repos/{owner_repo}/rulesets'
    method = ['-X', 'POST']
    if existing:
        path = f'{path}/{existing}'
        method = ['-X', 'PUT']
    if dry_run:
        return f'would {"update" if existing else "create"} ruleset {RULESET_NAME}'
    _, apply_err = gh_json([*method, path, '--input', '-'], body)
    if apply_err:
        return f'skip ruleset ({apply_err})'
    return f'{"updated" if existing else "created"} ruleset {RULESET_NAME}'


def apply_classic(owner_repo: str, branch: str, dry_run: bool) -> str:
    path = f'repos/{owner_repo}/branches/{branch}/protection'
    if dry_run:
        return f'would PUT classic protection on {branch}'
    _, err = gh_json(['-X', 'PUT', path, '--input', '-'], CLASSIC_PROTECTION)
    if err:
        return f'skip classic protection ({err})'
    return f'applied classic protection on {branch} (enforce_admins, 1 review)'


def main() -> int:
    parser = argparse.ArgumentParser(description='Apply main-branch protection')
    parser.add_argument('--repo', help='owner/name (defaults to the current gh repo)')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    owner_repo, default_branch = repo_info(args.repo)
    print(f'repo: {owner_repo} (default branch {default_branch})')
    if default_branch != 'main':
        RULESET_BODY['conditions']['ref_name']['include'] = [f'refs/heads/{default_branch}']
        print(f'note: protecting {default_branch}, not main')

    print(apply_ruleset(owner_repo, args.dry_run))
    print(apply_classic(owner_repo, default_branch, args.dry_run))
    print(
        'main (or the default branch) should now reject direct pushes and '
        'require a pull request with one approving review.'
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())

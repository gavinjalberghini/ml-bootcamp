#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Protect a student repo's main: no direct push; PRs need one approving review.

Mentor-only. Students have Write, not Admin, so they cannot change these
rules. Org owners can still push (needed for deploy). Prefer
`setup_org_rules.py` once per org; this script is the per-repo backup.

Usage:
    python3 scripts/setup_github_rules.py --repo org/ml-bootcamp-jane
    python3 scripts/setup_github_rules.py --repo org/ml-bootcamp-jane --dry-run
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gh_api import gh_json

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

# Students are Write, not Admin. Leave enforce_admins off so org owners can
# still push the first main (and hotfixes) without a student approval.
CLASSIC_PROTECTION = {
    'required_status_checks': None,
    'enforce_admins': False,
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


def repo_info(repo: str | None):
    cmd = ['gh', 'repo', 'view']
    if repo:
        cmd.append(repo)
    cmd.extend(['--json', 'nameWithOwner,defaultBranchRef'])
    import subprocess

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
    return f'applied classic protection on {branch} (1 review; admins may push)'


def run(repo: str | None = None, dry_run: bool = False) -> list[str]:
    if dry_run and repo:
        RULESET_BODY['conditions']['ref_name']['include'] = ['refs/heads/main']
        return [
            f'repo: {repo} (dry-run)',
            apply_ruleset(repo, True),
            apply_classic(repo, 'main', True),
        ]
    owner_repo, default_branch = repo_info(repo)
    lines = [f'repo: {owner_repo} (default branch {default_branch})']
    if default_branch != 'main':
        RULESET_BODY['conditions']['ref_name']['include'] = [f'refs/heads/{default_branch}']
        lines.append(f'note: protecting {default_branch}, not main')
    lines.append(apply_ruleset(owner_repo, dry_run))
    lines.append(apply_classic(owner_repo, default_branch, dry_run))
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description='Apply main-branch protection')
    parser.add_argument('--repo', help='owner/name (defaults to the current gh repo)')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    for line in run(repo=args.repo, dry_run=args.dry_run):
        print(line)
    print(
        'main should reject direct pushes from Write collaborators and '
        'require a pull request with one approving review.'
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Apply an org ruleset so student repos cannot update main except by reviewed PR.

Targets repositories named `ml-bootcamp-*` (not the source repo `ml-bootcamp`).
Org owners can bypass so `deploy_student.py` can push the first `main`.

Usage:
    python3 scripts/setup_org_rules.py --org my-org
    python3 scripts/setup_org_rules.py --org my-org --dry-run
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gh_api import gh_json

RULESET_NAME = 'protect-student-main'

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


def ruleset_body(include: list[str], exclude: list[str]) -> dict:
    return {
        'name': RULESET_NAME,
        'target': 'branch',
        'enforcement': 'active',
        'bypass_actors': [
            {
                'actor_id': 1,
                'actor_type': 'OrganizationAdmin',
                'bypass_mode': 'always',
            }
        ],
        'conditions': {
            'ref_name': {
                'include': ['refs/heads/main'],
                'exclude': [],
            },
            'repository_name': {
                'include': include,
                'exclude': exclude,
            },
        },
        'rules': [
            {'type': 'deletion'},
            {'type': 'non_fast_forward'},
            PULL_REQUEST_RULE,
        ],
    }


def find_ruleset_id(org: str):
    data, err = gh_json([f'orgs/{org}/rulesets'])
    if err:
        return None, err
    if not isinstance(data, list):
        return None, 'unexpected org ruleset list'
    for item in data:
        if item.get('name') == RULESET_NAME:
            return item.get('id'), None
    return None, None


def apply(org: str, include: list[str], exclude: list[str], dry_run: bool) -> tuple[str, int]:
    if dry_run:
        return (
            f'would create-or-update org ruleset {RULESET_NAME} on {org} ({include})',
            0,
        )
    body = ruleset_body(include, exclude)
    existing, err = find_ruleset_id(org)
    if err:
        return f'failed to list org rulesets ({err})', 1
    path = f'orgs/{org}/rulesets'
    method = ['-X', 'POST']
    action = 'create'
    if existing:
        path = f'{path}/{existing}'
        method = ['-X', 'PUT']
        action = 'update'
    _, apply_err = gh_json([*method, path, '--input', '-'], body)
    if apply_err:
        return f'failed to {action} org ruleset ({apply_err})', 1
    return f'{action}d org ruleset {RULESET_NAME} on {org}', 0


def main() -> int:
    parser = argparse.ArgumentParser(description='Apply org ruleset for student repos')
    parser.add_argument('--org', required=True, help='GitHub organization login')
    parser.add_argument(
        '--include',
        default='ml-bootcamp-*',
        help='repository_name include pattern (default: ml-bootcamp-*)',
    )
    parser.add_argument(
        '--exclude',
        default='ml-bootcamp',
        help='repository_name exclude pattern (default: ml-bootcamp)',
    )
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    include = [part.strip() for part in args.include.split(',') if part.strip()]
    exclude = [part.strip() for part in args.exclude.split(',') if part.strip()]
    print(json.dumps({'org': args.org, 'include': include, 'exclude': exclude}, indent=2))
    message, code = apply(args.org, include, exclude, args.dry_run)
    print(message)
    if code == 0:
        print(
            'Student repos matching the pattern require a pull request and one '
            'approving review to update main. Org owners can still push (for deploy).'
        )
    return code


if __name__ == '__main__':
    sys.exit(main())

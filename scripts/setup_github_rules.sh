#!/usr/bin/env bash
# Protect a student repo's main: no direct push; PRs need one approving review.
#
# Mentor-only. Students have Write, not Admin. Prefer setup_org_rules.sh once
# per org; this is the per-repo backup.
#
#   scripts/setup_github_rules.sh --repo org/ml-bootcamp-jane
#   scripts/setup_github_rules.sh --repo org/ml-bootcamp-jane --dry-run
set -euo pipefail

REPO=""
DRY_RUN=0
RULESET_NAME="protect-main"

die() {
  printf '%s\n' "$*" >&2
  exit 1
}

usage() {
  sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'
  exit 2
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      REPO="${2:-}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h | --help)
      usage
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
done

if [[ "$DRY_RUN" -eq 1 && -n "$REPO" ]]; then
  owner_repo="$REPO"
  default_branch="main"
  printf 'repo: %s (dry-run)\n' "$owner_repo"
else
  view=(gh repo view)
  if [[ -n "$REPO" ]]; then
    view+=( "$REPO" )
  fi
  owner_repo="$("${view[@]}" --json nameWithOwner --jq .nameWithOwner)" \
    || die "gh repo view failed; run gh auth login"
  default_branch="$("${view[@]}" --json defaultBranchRef --jq '.defaultBranchRef.name // "main"')"
  default_branch="${default_branch:-main}"
  printf 'repo: %s (default branch %s)\n' "$owner_repo" "$default_branch"
fi

if [[ "$default_branch" != "main" ]]; then
  printf 'note: protecting %s, not main\n' "$default_branch"
fi

ruleset_body() {
  local branch="$1"
  cat <<EOF
{
  "name": "${RULESET_NAME}",
  "target": "branch",
  "enforcement": "active",
  "bypass_actors": [],
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/${branch}"],
      "exclude": []
    }
  },
  "rules": [
    {"type": "deletion"},
    {"type": "non_fast_forward"},
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 1,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false,
        "allowed_merge_methods": ["merge", "squash", "rebase"]
      }
    }
  ]
}
EOF
}

classic_body() {
  cat <<'EOF'
{
  "required_status_checks": null,
  "enforce_admins": false,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": false,
    "required_approving_review_count": 1,
    "require_last_push_approval": false
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_conversation_resolution": false,
  "lock_branch": false,
  "allow_fork_syncing": true
}
EOF
}

if [[ "$DRY_RUN" -eq 1 ]]; then
  printf 'would create-or-update ruleset %s\n' "$RULESET_NAME"
  printf 'would PUT classic protection on %s\n' "$default_branch"
else
  existing_id="$(gh api "repos/${owner_repo}/rulesets" --jq ".[] | select(.name==\"${RULESET_NAME}\") | .id" 2>/dev/null || true)"
  if [[ -n "$existing_id" ]]; then
    if gh api -X PUT "repos/${owner_repo}/rulesets/${existing_id}" --input - <<<"$(ruleset_body "$default_branch")" >/dev/null; then
      printf 'updated ruleset %s\n' "$RULESET_NAME"
    else
      printf 'skip ruleset (update failed)\n'
    fi
  else
    if gh api -X POST "repos/${owner_repo}/rulesets" --input - <<<"$(ruleset_body "$default_branch")" >/dev/null; then
      printf 'created ruleset %s\n' "$RULESET_NAME"
    else
      printf 'skip ruleset (create failed)\n'
    fi
  fi
  if gh api -X PUT "repos/${owner_repo}/branches/${default_branch}/protection" --input - <<<"$(classic_body)" >/dev/null; then
    printf 'applied classic protection on %s (1 review; admins may push)\n' "$default_branch"
  else
    printf 'skip classic protection\n'
  fi
fi

printf '%s\n' \
  'main should reject direct pushes from Write collaborators and require a pull request with one approving review.'

#!/usr/bin/env bash
# Apply an org ruleset so student repos cannot update main except by reviewed PR.
#
# Targets repositories named ml-bootcamp-* (not the source repo ml-bootcamp).
# Org owners can bypass so deploy_student.sh can push the first main.
#
#   scripts/setup_org_rules.sh --org my-org
#   scripts/setup_org_rules.sh --org my-org --dry-run
set -euo pipefail

ORG=""
INCLUDE="ml-bootcamp-*"
EXCLUDE="ml-bootcamp"
DRY_RUN=0
RULESET_NAME="protect-student-main"

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
    --org)
      ORG="${2:-}"
      shift 2
      ;;
    --include)
      INCLUDE="${2:-}"
      shift 2
      ;;
    --exclude)
      EXCLUDE="${2:-}"
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

[[ -n "$ORG" ]] || die "pass --org"

# Turn comma-separated patterns into a JSON string array.
json_string_array() {
  local IFS=','
  local -a parts
  local first=1
  printf '['
  for part in $1; do
    part="${part#"${part%%[![:space:]]*}"}"
    part="${part%"${part##*[![:space:]]}"}"
    [[ -n "$part" ]] || continue
    if [[ "$first" -eq 1 ]]; then
      first=0
    else
      printf ', '
    fi
    printf '"%s"' "$part"
  done
  printf ']'
}

include_json="$(json_string_array "$INCLUDE")"
exclude_json="$(json_string_array "$EXCLUDE")"

printf 'org: %s\ninclude: %s\nexclude: %s\n' "$ORG" "$include_json" "$exclude_json"

if [[ "$DRY_RUN" -eq 1 ]]; then
  printf 'would create-or-update org ruleset %s on %s\n' "$RULESET_NAME" "$ORG"
  printf '%s\n' \
    'Student repos matching the pattern require a pull request and one approving review to update main. Org owners can still push (for deploy).'
  exit 0
fi

ruleset_body() {
  cat <<EOF
{
  "name": "${RULESET_NAME}",
  "target": "branch",
  "enforcement": "active",
  "bypass_actors": [
    {
      "actor_id": 1,
      "actor_type": "OrganizationAdmin",
      "bypass_mode": "always"
    }
  ],
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/main"],
      "exclude": []
    },
    "repository_name": {
      "include": ${include_json},
      "exclude": ${exclude_json}
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

existing_id="$(gh api "orgs/${ORG}/rulesets" --jq ".[] | select(.name==\"${RULESET_NAME}\") | .id" 2>/dev/null || true)"
if [[ -n "$existing_id" ]]; then
  gh api -X PUT "orgs/${ORG}/rulesets/${existing_id}" --input - <<<"$(ruleset_body)" >/dev/null \
    || die "failed to update org ruleset"
  printf 'updated org ruleset %s on %s\n' "$RULESET_NAME" "$ORG"
else
  gh api -X POST "orgs/${ORG}/rulesets" --input - <<<"$(ruleset_body)" >/dev/null \
    || die "failed to create org ruleset"
  printf 'created org ruleset %s on %s\n' "$RULESET_NAME" "$ORG"
fi

printf '%s\n' \
  'Student repos matching the pattern require a pull request and one approving review to update main. Org owners can still push (for deploy).'

#!/usr/bin/env bash
# Instantiate a student repo in a mentor-owned GitHub organization.
#
# Creates org/ml-bootcamp-<student> from this source tree, invites the
# student with Write (not Admin), opens the assignment issues, and applies
# per-repo main-branch protection. Run once per mentee as an org owner:
#
#   scripts/deploy_student.sh --org my-org --student jane
#   scripts/deploy_student.sh --org my-org --student jane --dry-run
#
# Does not take a student PAT. Uses your gh auth login session.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ORG="${ML_BOOTCAMP_ORG:-}"
STUDENT=""
NAME=""
REF=""
VISIBILITY="private"
ORG_MEMBER=0
FORCE_SOURCE=0
SKIP_PUSH=0
SKIP_INVITE=0
SKIP_ISSUES=0
SKIP_RULES=0
DRY_RUN=0
PREFIX="ml-bootcamp"

die() {
  printf '%s\n' "$*" >&2
  exit 1
}

usage() {
  sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//'
  exit 2
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --org)
      ORG="${2:-}"
      shift 2
      ;;
    --student)
      STUDENT="${2:-}"
      shift 2
      ;;
    --name)
      NAME="${2:-}"
      shift 2
      ;;
    --ref)
      REF="${2:-}"
      shift 2
      ;;
    --public)
      VISIBILITY="public"
      shift
      ;;
    --org-member)
      ORG_MEMBER=1
      shift
      ;;
    --force-source)
      FORCE_SOURCE=1
      shift
      ;;
    --skip-push)
      SKIP_PUSH=1
      shift
      ;;
    --skip-invite)
      SKIP_INVITE=1
      shift
      ;;
    --skip-issues)
      SKIP_ISSUES=1
      shift
      ;;
    --skip-rules)
      SKIP_RULES=1
      shift
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

[[ -n "$ORG" ]] || die "pass --org or set ML_BOOTCAMP_ORG"
[[ -n "$STUDENT" ]] || die "pass --student"

if [[ ! "$STUDENT" =~ ^[A-Za-z0-9]([A-Za-z0-9-]{0,37}[A-Za-z0-9])?$ ]]; then
  die "invalid GitHub login: $STUDENT"
fi

if [[ -z "$NAME" ]]; then
  NAME="${PREFIX}-$(printf '%s' "$STUDENT" | tr '[:upper:]' '[:lower:]')"
fi
owner_repo="${ORG}/${NAME}"

resolve_ref() {
  if [[ -n "$REF" ]]; then
    git -C "$ROOT" rev-parse --verify "$REF" >/dev/null
    printf '%s\n' "$REF"
    return
  fi
  local candidate
  for candidate in main origin/main; do
    if git -C "$ROOT" rev-parse --verify "$candidate" >/dev/null 2>&1; then
      printf '%s\n' "$candidate"
      return
    fi
  done
  printf 'HEAD\n'
}

ref="$(resolve_ref)"
description="ML bootcamp classification sequence for ${STUDENT}"

printf 'source: %s\n' "$ROOT"
printf 'ref:    %s\n' "$ref"
printf 'dest:   %s (%s)\n' "$owner_repo" "$VISIBILITY"
printf 'student Write: %s\n' "$STUDENT"

if gh repo view "$owner_repo" --json nameWithOwner >/dev/null 2>&1; then
  printf 'exists %s\n' "$owner_repo"
elif [[ "$DRY_RUN" -eq 1 ]]; then
  printf 'would create %s (%s)\n' "$owner_repo" "$VISIBILITY"
else
  gh repo create "$owner_repo" "--${VISIBILITY}" --disable-wiki --description "$description" \
    || die "failed to create $owner_repo"
  printf 'created %s\n' "$owner_repo"
fi

if [[ "$SKIP_PUSH" -eq 0 ]]; then
  if [[ "$DRY_RUN" -eq 1 ]]; then
    if [[ "$FORCE_SOURCE" -eq 1 ]]; then
      printf 'would git push %s -> %s main (force)\n' "$ref" "$owner_repo"
    else
      printf 'would git push %s -> %s main\n' "$ref" "$owner_repo"
    fi
  else
    token="$(gh auth token)" || die "gh auth token failed; run gh auth login as an org owner"
    [[ -n "$token" ]] || die "gh auth token failed; run gh auth login as an org owner"
    push=(git -C "$ROOT" push)
    if [[ "$FORCE_SOURCE" -eq 1 ]]; then
      push+=(--force)
    fi
    if ! "${push[@]}" "https://x-access-token:${token}@github.com/${owner_repo}.git" "${ref}:refs/heads/main"; then
      die "push failed. If main already has student work, do not --force-source. If this is a brand-new repo, check org rulesets / your owner access."
    fi
    printf 'pushed %s to %s main\n' "$ref" "$owner_repo"
  fi
fi

if [[ "$ORG_MEMBER" -eq 1 ]]; then
  if gh api "orgs/${ORG}/members/${STUDENT}" >/dev/null 2>&1; then
    printf '%s is already an org member\n' "$STUDENT"
  elif [[ "$DRY_RUN" -eq 1 ]]; then
    printf 'would invite %s to org %s as a member\n' "$STUDENT" "$ORG"
  else
    user_id="$(gh api "users/${STUDENT}" --jq .id)" \
      || die "cannot resolve GitHub user $STUDENT"
    if gh api -X POST "orgs/${ORG}/invitations" --input - <<<"{\"invitee_id\": ${user_id}, \"role\": \"direct_member\"}" >/dev/null; then
      printf 'invited %s to org %s\n' "$STUDENT" "$ORG"
    else
      die "failed to invite $STUDENT to org $ORG"
    fi
  fi
fi

if [[ "$SKIP_INVITE" -eq 0 ]]; then
  if [[ "$DRY_RUN" -eq 1 ]]; then
    printf 'would invite %s to %s with Write\n' "$STUDENT" "$owner_repo"
  else
    gh api -X PUT "repos/${owner_repo}/collaborators/${STUDENT}" -f permission=push >/dev/null \
      || die "failed to invite ${STUDENT}. If the org forbids outside collaborators, add them as an org member first (--org-member) or invite them in the GitHub UI."
    printf 'invited %s on %s (Write)\n' "$STUDENT" "$owner_repo"
  fi
fi

extra=()
if [[ "$DRY_RUN" -eq 1 ]]; then
  extra+=(--dry-run)
fi

if [[ "$SKIP_ISSUES" -eq 0 ]]; then
  "$ROOT/scripts/create_issues.sh" --repo "$owner_repo" "${extra[@]+"${extra[@]}"}"
fi

if [[ "$SKIP_RULES" -eq 0 ]]; then
  "$ROOT/scripts/setup_github_rules.sh" --repo "$owner_repo" "${extra[@]+"${extra[@]}"}"
fi

printf '\nStudent URL: https://github.com/%s\n' "$owner_repo"
printf 'Ask them to accept the invite, then start at the [git] issue.\n'

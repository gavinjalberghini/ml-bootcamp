#!/usr/bin/env bash
# Create GitHub issues from issues/NN-*.md using the gh CLI.
# Index files (README.md) are not tickets. Idempotent: skips a title
# that already exists (open or closed).
#
#   scripts/create_issues.sh --repo owner/name
#   scripts/create_issues.sh --dry-run
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO=""
DRY_RUN=0

die() {
  printf '%s\n' "$*" >&2
  exit 1
}

usage() {
  sed -n '2,7p' "$0" | sed 's/^# \{0,1\}//'
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

shopt -s nullglob
files=("$ROOT"/issues/[0-9][0-9]-*.md)
[[ ${#files[@]} -gt 0 ]] || die "no issue files found in issues/ (expected NN-slug.md)"

existing=""
if [[ "$DRY_RUN" -eq 0 ]]; then
  list_cmd=(gh issue list --state all --limit 200 --json title --jq '.[].title')
  if [[ -n "$REPO" ]]; then
    list_cmd+=(--repo "$REPO")
  fi
  existing="$("${list_cmd[@]}")"
fi

created=0
for path in "${files[@]}"; do
  first="$(head -n 1 "$path")"
  [[ "$first" == '# '* ]] || die "$path must start with a \"# title\" line"
  title="${first#\# }"
  if [[ -n "$existing" ]] && printf '%s\n' "$existing" | grep -Fxq -- "$title"; then
    printf '%s: skip (exists) %s\n' "$(basename "$path")" "$title"
    continue
  fi
  printf '%s: %s\n' "$(basename "$path")" "$title"
  if [[ "$DRY_RUN" -eq 1 ]]; then
    created=$((created + 1))
    continue
  fi
  body_file="$(mktemp)"
  tail -n +2 "$path" | sed -e '/./,$!d' >"$body_file"
  create_cmd=(gh issue create --title "$title" --body-file "$body_file")
  if [[ -n "$REPO" ]]; then
    create_cmd+=(--repo "$REPO")
  fi
  "${create_cmd[@]}"
  rm -f "$body_file"
  created=$((created + 1))
done

printf 'issues: %s created or already present\n' "$created"

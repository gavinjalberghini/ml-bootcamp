# Commit messages

This repo uses [Conventional Commits](https://www.conventionalcommits.org/)
with a required scope, the same `type(scope):` shape as
[pkgxdev/pantry](https://github.com/pkgxdev/pantry) (`fix(llama.cpp): …`).

CI runs `scripts/lint_commits.py` on every pull request.

## Format

```text
type(scope): description
```

The **entire first line** must be 1–72 characters. A blank line, then an
optional body, is fine. Merge commits and `Revert "…"` commits are ignored.

### Types

| Type | Use |
| --- | --- |
| `feat` | New behavior (a method, a report section, a flag) |
| `fix` | Correct a bug in something already started |
| `docs` | Readings, answers, README, comments only |
| `chore` | Tooling, notes that are not the assignment itself |
| `test` | Checks you added |
| `refactor` | Same behavior, clearer code |
| `style` | Formatting only |

### Scopes

Use the ticket slug, or one of the shared scopes:

```text
git
uv
taskfile
pa-knn
pa-scaled
pa-metrics
pa-selection
pa-ensemble
pa-gpu
pa-online
ra-types
ra-scaling
ra-selection
ra-ensembles
ra-streaming
ra-hardware
ra-drift
ra-imbalance
ra-cost
lr-jetson
lr-slam
repo
docs
data
ci
```

### Description

Imperative mood, no trailing period: `implement leave-one-out`, not
`implemented leave-one-out.` or `WIP knn`.

## Examples

```text
docs(git): fill in the learning log
feat(uv): run hello.py with in-file metadata
feat(taskfile): add hello and echo-vars tasks
docs(ra-types): answer classification prompts
feat(pa-knn): implement leave-one-out kNN
fix(pa-knn): exclude the query row from the pool
feat(pa-scaled): add pool-only z-score and minmax
docs(ra-scaling): explain wine feature dominance
feat(pa-metrics): add baseline and macro-F1
chore(data): regenerate stream files
ci(repo): apply main-branch ruleset
```

## Rejected

```text
updated knn
PA1 done
fix knn
feat: implement knn
feat(PA1): implement knn
feat(pa-knn): Implement leave-one-out kNN.
```

# Mentor scripts

These run against a GitHub organization you own. They use your
`gh auth login` session. Students never supply a PAT.

| Script | What it does |
| --- | --- |
| [`deploy_student.sh`](deploy_student.sh) | Create `ORG/ml-bootcamp-<login>`, push this tree, invite Write, open issues, protect `main` |
| [`create_issues.sh`](create_issues.sh) | Open one issue per `issues/NN-*.md` (skips titles that already exist) |
| [`setup_org_rules.sh`](setup_org_rules.sh) | Org ruleset: reviewed PRs into `main` on `ml-bootcamp-*` |
| [`setup_github_rules.sh`](setup_github_rules.sh) | Per-repo `main` protection (backup if the org ruleset is missing) |
| [`lint_commits.py`](lint_commits.py) | Conventional-commit subject lint (`type(scope): …`) |

Typical path: [docs/mentor.md](../docs/mentor.md).

```bash
scripts/setup_org_rules.sh --org YOUR_ORG
scripts/deploy_student.sh --org YOUR_ORG --student github-login
scripts/create_issues.sh --repo YOUR_ORG/ml-bootcamp-login --dry-run
```

Root Task wrappers: `task deploy`, `task org-rules`, `task issues`,
`task github-rules`, `task lint-commits`.

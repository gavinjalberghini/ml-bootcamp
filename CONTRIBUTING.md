# Contributing

This repository is the **curriculum source**, not a place to turn in
homework. Student work happens in `ORG/ml-bootcamp-<login>`, created by
[`scripts/deploy_student.sh`](scripts/deploy_student.sh).

## Students

You already have a private repo. Do not open assignment PRs here.

- Start at the [git](issues/00-git.md) issue in **your** repo.
- Branch as `<slug>/<short-topic>`, never commit to `main`.
- Commit as `type(scope): description`
  ([`.github/commit-convention.md`](.github/commit-convention.md)).
- One ticket per PR. Wait for mentor review.

## Mentors

Follow [docs/mentor.md](docs/mentor.md) to instantiate a student. Changes to
the sequence itself belong in this source repo, then re-deploy (or
`--force-source` only on a repo with no student commits).

## Changing the source

Keep slugs aligned across four places when you add or rename a ticket:

1. `issues/NN-slug.md` — first line is the GitHub issue title
2. `learning/<slug>/` — student path
3. `Taskfile.yml` — `task` name for programming assignments
4. `.github/commit-convention.md` — allowed `scope`

`scripts/create_issues.sh` only opens files matching `issues/NN-*.md`.
Index files such as `issues/README.md` are not tickets.

PRs into `main` on this repo use the same commit convention and the
[pull request template](.github/pull_request_template.md).

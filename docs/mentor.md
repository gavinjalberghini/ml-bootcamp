# Mentor runbook

This is the source of truth for the mentorship. Students do not own their
repo and do not hand over a PAT. You instantiate a **student repo inside a
GitHub organization you own**.

Give students **Write** on their repo only, not Admin and not org Owner.
Invite them as an outside collaborator, or as an org member with no default
repository access.

## One-time org setup

1. Create a GitHub organization (free orgs can hold private repos).
2. Keep this repository as the source of truth. You can leave it on your
   user account or move it into the org as `ml-bootcamp` (not
   `ml-bootcamp-*`).
3. Install the [GitHub CLI](https://cli.github.com/) and `gh auth login` as
   an **org owner**.
4. Apply the org ruleset so every student repo requires a reviewed PR into
   `main`. Org owners can still push (so deploy works):

   ```bash
   scripts/setup_org_rules.sh --org YOUR_ORG
   ```

   The ruleset matches `ml-bootcamp-*` and skips `ml-bootcamp`.

## Instantiate a student

From a clone of this source repo, after `gh auth login`:

```bash
scripts/deploy_student.sh --org YOUR_ORG --student github-login
```

That command:

1. Creates `YOUR_ORG/ml-bootcamp-<login>` (private by default).
2. Pushes this source tree to that repo’s `main`.
3. Invites the student with **Write**.
4. Opens one GitHub issue per ticket file in `issues/` (`NN-slug.md`).
5. Applies per-repo `main` protection (backup for the org ruleset).

Optional flags: `--public`, `--name other-repo`, `--ref main`,
`--org-member`, `--dry-run`. Re-running skips existing issues and does not
overwrite student commits unless you pass `--force-source`.

```bash
export ML_BOOTCAMP_ORG=YOUR_ORG
task deploy -- --student github-login
task org-rules
```

Tell the student the repo URL and that they should start at the **git**
issue. You already have access; they open PRs, you review.

At the end of the mentorship they can fork the repo to their account if
they want a portfolio copy.

Script details: [scripts/README.md](../scripts/README.md).

## Reviewing work

Tickets are procedures. After each PR, check that the new class
**subclasses** the previous one and did not paste a second distance function.
Common failures: query row in leave-one-out, scaler fit on the whole file,
accuracy-only reports, unscaled wine distances, copying `pa-knn` instead of
`import_pa`. Stretch goals are optional; do not block a PR that skipped
them. Do block a PR that broke the required class API in order to attempt
one.

## Source repo on GitHub

The About sidebar is not a file. On the source repo, set:

- **Description:** Mentored applied-ML classification sequence. Students implement kNN from scratch; mentors instantiate private student repos.
- **Topics:** `machine-learning`, `education`, `knn`, `mentorship`, `python`, `uv`
- **License:** MIT (this repo’s `LICENSE` file)

Student repos already get a description from `deploy_student.sh`.

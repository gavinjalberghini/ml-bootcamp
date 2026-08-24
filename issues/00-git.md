# [git] Own This Repository

You need: a GitHub account and Git installed.

You will: clone **this** repository (your copy of the template), set up the
branch and commit rules this mentorship uses, prove the review loop works,
and stop. Do not start `pa-knn` yet. The next ticket installs Python and uv.

## Rules you will follow on every later ticket

These are not optional style notes. CI and GitHub will reject work that
breaks them.

### Branches

- Never commit, push, or merge directly to `main`.
- One branch per ticket (or per focused follow-up). Name it
  `<slug>/<short-topic>`:
  - `git/setup`
  - `uv/hello`
  - `pa-knn/leave-one-out`
  - `ra-types/answers`
- Do not reuse a finished branch for the next assignment.

### Commit messages

Same shape as [pkgxdev/pantry](https://github.com/pkgxdev/pantry):
Conventional Commits with a **scope**.

```text
type(scope): short description
```

- **type:** `feat`, `fix`, `docs`, `chore`, `test`, `refactor`, or `style`
- **scope:** the ticket slug (`git`, `uv`, `pa-knn`, `ra-types`, …) or
  `repo` / `data` / `ci` for shared files
- **description:** imperative, 1–72 characters for the whole first line

Examples:

```text
docs(git): fill in the learning log
feat(pa-knn): implement leave-one-out kNN
fix(pa-scaled): fit z-score on the pool only
docs(ra-scaling): answer leakage prompts
chore(uv): record python and uv versions
```

Not allowed: `updated knn`, `WIP`, `PA1 stuff`, a subject with no type and
scope. Full list: [`.github/commit-convention.md`](../.github/commit-convention.md).

### Pull requests

- Every change reaches `main` through a PR. There is no “just this once”
  push to `main`.
- Wait for your mentor to review and approve. Do not merge your own PR
  until they have approved it.
- Fill in the PR template (summary, why, how you checked the work).
- One ticket per PR unless a fix-up is clearly the same change.

## Steps

1. Install Git if `git --version` fails: [installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. Clone **this** repository, not the upstream template. Use the GitHub URL
   of the repo that was created for you.
3. Install the [GitHub CLI](https://cli.github.com/) and run `gh auth login`
   so later tickets can open PRs and apply rules. GitHub rejects account
   passwords on the command line; use `gh` or a
   [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
4. Invite your mentor as a collaborator with **Write** access
   (Settings → Collaborators). They need that role to approve PRs.
5. Apply the `main` protection rules (blocks direct pushes; PRs need one
   approving review). The script is stdlib-only; you do not need uv yet:

   ```bash
   python3 scripts/setup_github_rules.py
   ```

   After the [uv](01-uv.md) ticket you can use `task github-rules` instead.
   You must be the repo owner or an admin. If the API call fails, set the
   same rules in the GitHub UI (Settings → Rules → Rulesets, or Branches):
   no direct push to `main`, pull request required, one approving review,
   do not allow administrators to bypass.
6. Create a branch named `git/setup`.
7. Open `learning/README.md`. Fill in your name, a short background
   (coursework, languages, anything you already know about ML), and what you
   want to learn.
8. Commit that file with a conventional message:

   ```bash
   git add learning/README.md
   git commit -m "docs(git): fill in the learning log"
   ```

9. Push the branch and open a pull request into `main`. Ask your mentor to
   review it. Do not merge until they approve.

Later assignments use the same pattern: one slug-named branch, conventional
commits, one focused diff, one PR, mentor review.

## What to turn in

- A pull request that adds your filled-in `learning/README.md`.
- Evidence that `main` is protected (the rules script succeeded, or a
  screenshot / `gh` output in the PR description if the API call failed and
  you set the same rules in the GitHub UI).

## Stretch goal (optional)

Stretch goals are extra challenge. Skip this if you want. Nothing later
depends on it.

**Challenge:** In `learning/README.md` (or `learning/stretch.md` if you
prefer a separate file), explain clone / branch / conventional commit / PR
review in your own words as if you were teaching a classmate who has never
used Git. No extra tools required.

## Acceptance criteria

- The PR is open against `main` from a `git/…` branch, not from `main`.
- The README contains your name, background, and learning goals.
- Commit subjects on the PR match `type(scope): description`.
- The mentor is a collaborator, and `main` requires a pull request plus one
  approving review (script or equivalent UI settings).
- You can clone, branch, commit, push, and open a PR without help.
- Stretch is optional. Skipping it does not block [uv](01-uv.md).

## References

- [Git and GitHub for beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [`.github/commit-convention.md`](../.github/commit-convention.md)

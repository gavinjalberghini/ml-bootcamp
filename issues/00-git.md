# [git] The Review Loop

You need: a GitHub account, Git installed, and the invite your mentor sent
to a repository in their organization.

You will: accept that invite, clone **your** assigned repo, prove the
review loop works, and stop. You do not own this repository and you do not
change its settings. Do not start `pa-knn` yet. The next ticket installs
Python and uv.

## Rules you will follow on every later ticket

These are not optional style notes. CI and GitHub will reject work that
breaks them.

### Branches

- Never commit, push, or merge directly to `main`. GitHub will block it.
- One branch per ticket (or per focused follow-up). Name it
  `<slug>/<short-topic>`:
  - `git/setup`
  - `uv/hello`
  - `taskfile/setup`
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
2. Accept the GitHub invitation your mentor sent (email, or
   [github.com/notifications](https://github.com/notifications)). You should
   have **Write** access to a repo named like `ml-bootcamp-<you>` in their
   org. If you cannot see it, ask them — do not create your own copy.
3. Clone **that** repository. Use the URL they gave you, not this file’s
   upstream source.

   ```bash
   git clone https://github.com/ORG/ml-bootcamp-YOURLOGIN.git
   cd ml-bootcamp-YOURLOGIN
   ```

4. Optional but useful: install the [GitHub CLI](https://cli.github.com/)
   and run `gh auth login` so you can open PRs from the terminal. You can
   also open PRs in the GitHub website. GitHub rejects account passwords on
   the command line; use `gh` or a
   [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
   that you keep for yourself. Do not send a token to your mentor.
5. Create a branch named `git/setup`.
6. Open `learning/README.md`. Fill in your name, a short background
   (coursework, languages, anything you already know about ML), and what you
   want to learn.
7. Commit that file with a conventional message:

   ```bash
   git add learning/README.md
   git commit -m "docs(git): fill in the learning log"
   ```

8. Push the branch and open a pull request into `main`. Ask your mentor to
   review it. Do not merge until they approve.

   ```bash
   git push -u origin git/setup
   gh pr create
   ```

Later assignments use the same pattern: one slug-named branch, conventional
commits, one focused diff, one PR, mentor review.

## What to turn in

- A pull request that adds your filled-in `learning/README.md`.

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
- You can clone, branch, commit, push, and open a PR without help.
- Stretch is optional. Skipping it does not block [uv](01-uv.md).

## References

- [Git and GitHub for beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [`.github/commit-convention.md`](../.github/commit-convention.md)

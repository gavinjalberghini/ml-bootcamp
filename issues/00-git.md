# [git] The Review Loop

You need: a GitHub account, Git, and the invite your mentor sent to a repo
in their organization.

You will: accept that invite, clone **your** assigned repo, prove the
review loop, and stop. You do not own this repository and you do not
change its settings. Next ticket is uv.

## Rules (every later ticket)

CI and GitHub reject work that breaks these.

**Branches.** Never commit or push to `main`. One branch per ticket:
`<slug>/<short-topic>` (`git/setup`, `uv/hello`, `taskfile/setup`,
`pa-knn/leave-one-out`). Do not reuse a finished branch.

**Commits.** `type(scope): description` — same shape as
[pkgxdev/pantry](https://github.com/pkgxdev/pantry). Scope is the ticket
slug (`git`, `uv`, `taskfile`, `pa-knn`, …) or `repo` / `data` / `ci`.
The first line is at most 72 characters. Examples:

```text
docs(git): fill in the learning log
feat(pa-knn): implement leave-one-out kNN
```

Not allowed: `updated knn`, `WIP`, a subject with no type and scope.
Full list: `.github/commit-convention.md`.

**Pull requests.** Every change reaches `main` through a PR. Wait for
mentor approval before you merge. Fill in the PR template. One ticket per
PR unless a fix-up is clearly the same change.

## Steps

1. Install Git if `git --version` fails: [installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. Accept the GitHub invitation (email or
   [notifications](https://github.com/notifications)). You should have
   **Write** on a repo named like `ml-bootcamp-<you>`. If you cannot see
   it, ask your mentor — do not create your own copy.
3. Clone **that** URL, not the upstream source:

   ```bash
   git clone https://github.com/ORG/ml-bootcamp-YOURLOGIN.git
   cd ml-bootcamp-YOURLOGIN
   ```

4. Optional: install the [GitHub CLI](https://cli.github.com/) and run
   `gh auth login` so you can open PRs from the terminal. You can also use
   the website. Keep any personal access token to yourself.
5. Create a branch named `git/setup`.
6. Fill in `learning/README.md`: name, background, what you want to learn.
7. Commit:

   ```bash
   git add learning/README.md
   git commit -m "docs(git): fill in the learning log"
   ```

8. Push and open a PR into `main`. Do not merge until your mentor approves.

   ```bash
   git push -u origin git/setup
   gh pr create
   ```

Same pattern later: one slug-named branch, conventional commits, one
focused PR, mentor review.

## What to turn in

- A PR that adds your filled-in `learning/README.md`.

## Stretch goal (optional)

Skip if you want. Nothing later depends on it.

**Challenge:** In `learning/README.md`, explain clone / branch /
conventional commit / PR review as if teaching a classmate who has never
used Git.

## Acceptance criteria

- PR is against `main` from a `git/…` branch.
- README has your name, background, and learning goals.
- Commit subjects match `type(scope): description`.
- You can clone, branch, commit, push, and open a PR without help.
- Stretch is optional. Skipping it does not block uv.

## References

- [Git and GitHub for beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- `.github/commit-convention.md`

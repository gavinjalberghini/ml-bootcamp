# [Programming Assignment 0] Own This Repository

You need: a GitHub account and Git installed.

You will: clone **this** repository (your copy of the template), prove the
review loop works, and stop. Do not start PA1 yet. The next ticket installs
Python and uv.

## Steps

1. Install Git if `git --version` fails: [installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. Clone **this** repository, not the upstream template. Use the GitHub URL
   of the repo that was created for you.
3. Create a branch named `pa0-setup` (or similar). It does not need to be
   your personal name.
4. Open `learning/README.md`. Fill in your name, a short background
   (coursework, languages, anything you already know about ML), and what you
   want to learn.
5. Commit that file: `git add learning/README.md && git commit -m "PA0: learning log"`.
6. Push the branch and open a pull request into `main` (or `master`) so your
   mentor can review it.

Later assignments use the same pattern: one branch, one focused diff, one PR.

GitHub rejects account passwords on the command line. Use `gh auth login` or
a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## What to turn in

- A pull request that adds your filled-in `learning/README.md`.

## Acceptance criteria

- The PR is open against this repository's default branch.
- The README contains your name, background, and learning goals.
- You can clone, branch, commit, push, and open a PR without help.

## References

- [Git and GitHub for beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

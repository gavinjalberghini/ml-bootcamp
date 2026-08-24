# [taskfile] Install Task and write a Taskfile

You need: [git](00-git.md) and [uv](01-uv.md) done. `uv run learning/uv/hello.py`
works.

You will: install [Task](https://taskfile.dev/), read the repo’s root
`Taskfile.yml`, and write a **small Taskfile of your own**. Do not edit the
root `Taskfile.yml`. Later tickets call those task names (`knn`, `scaled`,
…). A broken root file blocks everyone after this.

## Steps

1. Install Task: follow [Task installation](https://taskfile.dev/installation/).
   Open a new terminal and run `task --version`. You want Task v3.
2. From the repo root run:

   ```bash
   task --list
   ```

   You should see `uv`, `knn`, mentor tasks, and others. If `task` is not
   found, the install did not land on your `PATH`.
3. Open the root `Taskfile.yml`. Read it. Note:
   - `version: '3'`
   - `vars` (`DATA`, `K`, `NORMALIZE`, …) and how a task uses `{{.K}}`
   - `dir:` on programming tasks so `uv run kNN.py` runs in that folder
   - `{{.ROOT_DIR}}` for paths that must stay repo-absolute
   - How `task knn` is the same idea as
     `uv run learning/pa-knn/kNN.py learning/resources/data/small.arff --k 3`
4. Run the uv wrapper you already proved by hand:

   ```bash
   task uv
   task setup
   ```

   Same hello line and Python version as the uv ticket.
5. Open `learning/taskfile/Taskfile.yml`. It is a skeleton. Keep
   `version: '3'`. Implement the required tasks (sudo comments are sketches,
   not copy-paste YAML):
   - `hello` — print exactly `hello from task`
   - `echo-vars` — print the `WHO` variable (default `student`). Someone
     else must be able to run `task echo-vars WHO=yourname` and see that
     value.
6. From the repo root run:

   ```bash
   task --taskfile learning/taskfile/Taskfile.yml hello
   task --taskfile learning/taskfile/Taskfile.yml echo-vars
   task --taskfile learning/taskfile/Taskfile.yml echo-vars WHO=mentor
   ```

   or the root shortcut `task taskfile` (it only calls `hello` on your
   file).
7. Write `learning/taskfile/notes.md` with:
   - `task --version`
   - In your own words: what a Taskfile is for, versus running `uv run`
     yourself
   - How you would pass a different data file into `task knn` (look at
     `DATA` / `DATA_ABS` in the root file)
   - One sentence on why this ticket’s Taskfile lives under
     `learning/taskfile/` and not in the repo root
8. On a branch named `taskfile/setup`, commit and open a pull request:

   ```bash
   git checkout -b taskfile/setup
   git add learning/taskfile
   git commit -m "feat(taskfile): add hello and echo-vars tasks"
   git push -u origin taskfile/setup
   gh pr create
   ```

## Command-line contract

Your file is `learning/taskfile/Taskfile.yml`. Required task names: `hello`,
`echo-vars`. Required var: `WHO` (default `student`). Do not rename the
root tasks.

## What to turn in

- Working `learning/taskfile/Taskfile.yml`
- `learning/taskfile/notes.md` answering the prompts in step 7

## Stretch goal (optional)

Stretch goals are extra challenge. Skip this if you want. Do not change
the root `Taskfile.yml` for this.

**Challenge:** In `learning/taskfile/Taskfile.yml` add a `wrap-uv` task that
runs `uv run` on `learning/uv/hello.py` using a repo-root path (so it works
no matter what your current directory is). Write what you did in
`learning/taskfile/stretch.md`. `task taskfile` must still only need
`hello`.

## Acceptance criteria

- `task --version` works.
- `task --list` from the repo root shows the provided assignment tasks.
- `task --taskfile learning/taskfile/Taskfile.yml hello` prints `hello from task`.
- `echo-vars` prints `student` by default and honors `WHO=…`.
- The root `Taskfile.yml` is unchanged.
- `learning/taskfile/notes.md` answers the prompts.
- Stretch is optional. Skipping it does not block [ra-types](03-ra-types.md).

## References

- [Installing Task](https://taskfile.dev/installation/)
- [Taskfile schema](https://taskfile.dev/docs/guide)
- [Variables](https://taskfile.dev/docs/guide#variables)
- [CLI](https://taskfile.dev/docs/usage)

# ML Bootcamp

Template repository for a mentorship in applied machine learning classification.
Each student gets their own copy of this repo and owns it: the issues, the
branches, and the pull requests. Work happens under `learning/`. Shared data
and tooling live in `learning/resources/`.

kNN is the only algorithm you implement. Each programming assignment **imports
the previous class** and adds one facet. Fix a bug where you introduced it.

Tickets use **slugs** that match folders and Task names: `pa-knn`,
`ra-scaling`, `lr-jetson`. Table order is learning order.

## Git and GitHub

Do not commit or push to `main`. Every change goes on a branch, then a pull
request, then mentor review. Commit subjects follow Conventional Commits
with a ticket scope, the same `type(scope):` shape used in
[pkgxdev/pantry](https://github.com/pkgxdev/pantry):

```text
feat(pa-knn): implement leave-one-out kNN
docs(ra-types): answer problem-type prompts
```

The first ticket ([git](issues/00-git.md)) walks through branch names, the
message format, and applying repo rules so GitHub rejects direct pushes to
`main` and requires one approving review. After that:

```bash
task github-rules
```

CI on every PR checks commit subjects (`scripts/lint_commits.py`). Details:
[`.github/commit-convention.md`](.github/commit-convention.md).

## Python and uv

Assignments are [uv](https://docs.astral.sh/uv/) **scripts**, not a project
venv. Each `learning/<slug>/…py` file starts with a [PEP 723](https://peps.python.org/pep-0723/)
header. `uv run that_file.py` reads **that file's** `requires-python` and
`dependencies`. There is nothing to activate.

Install Python 3.10+ and uv in the [uv](issues/01-uv.md) ticket (after
[git](issues/00-git.md)). Then:

```bash
uv run learning/uv/hello.py
uv run learning/pa-knn/kNN.py learning/resources/data/small.arff
```

[Task](https://taskfile.dev/installation/) is optional sugar (`task knn`
is the same `uv run`).

Third-party packages are declared in the file that uses them (matplotlib in
`pa-metrics` / `pa-selection`; optional CuPy in `pa-gpu`'s header). Importing
an earlier script does **not** inherit its uv dependencies — re-list anything
you still call.

## How code is reused

`learning/load_assignment.py` loads an earlier assignment as a module.

| You write | Class | Imports |
| --- | --- | --- |
| `pa-knn` | `KNN` | — |
| `pa-scaled` | `ScaledKNN(KNN)` | `pa-knn` |
| `pa-metrics` | `ReportingKNN(ScaledKNN)` | `pa-scaled` |
| `pa-selection` | `SelectingKNN(ScaledKNN)` | `pa-scaled` + `pa-metrics` |
| `pa-ensemble` | `EnsembleKNN(ScaledKNN)` | `pa-scaled` + `pa-metrics` |
| `pa-gpu` | `GpuKNN(ScaledKNN)` | `pa-scaled` + `pa-metrics` |
| `pa-online` | `OnlineKNN(ScaledKNN)` | `pa-scaled` + `pa-metrics` |

Do not copy `kNN.py` into the next folder. The skeletons already call
`import_pa('pa-knn')` (or `pa-scaled` / `pa-metrics`). Keep the class names.

Required methods include a **sudo** comment: a vague sketch of the idea, not
runnable Python. Rewrite it yourself. Do not paste it as code.

## Stretch goals

Every ticket has an optional stretch goal. Its job is to pose a harder
challenge after the required work is done — not to unlock the next
assignment.

- Skip any stretch you want. The next ticket never imports stretch methods
  and never requires `stretch.md`.
- Put stretch writeups in `learning/<assignment>/stretch.md` (or the extra
  heading in a reading's `answers.md`).
- Do not change required method names or the `none` / `zscore` / `minmax`
  contract to “finish” a stretch. Isolation is the point: a failed stretch
  must not break `pa-scaled` importing `pa-knn`.

## Assignments

Do them in **table order**. The slug is the ID.

| Ticket | Path | You leave behind |
| --- | --- | --- |
| [git](issues/00-git.md) | `learning/README.md` | owned repo, first PR, branch rules |
| [uv](issues/01-uv.md) | `learning/uv/` | uv + in-file deps |
| [ra-types](issues/02-ra-types.md) | `learning/ra-types/answers.md` | problem types for these files |
| [pa-knn](issues/03-pa-knn.md) | `learning/pa-knn/kNN.py` | class `KNN`, leave-one-out |
| [ra-scaling](issues/04-ra-scaling.md) | `learning/ra-scaling/answers.md` | why scale, how not to leak |
| [pa-scaled](issues/05-pa-scaled.md) | `learning/pa-scaled/kNN_scaled.py` | `ScaledKNN`, `--normalize`, `--task` |
| [pa-metrics](issues/06-pa-metrics.md) | `learning/pa-metrics/kNN_report.py` | `ReportingKNN`, baseline, plots |
| [ra-selection](issues/07-ra-selection.md) | `learning/ra-selection/answers.md` | validation vs test |
| [pa-selection](issues/08-pa-selection.md) | `learning/pa-selection/kNN_select.py` | `k` sweep, vote fractions |
| [ra-ensembles](issues/09-ra-ensembles.md) | `learning/ra-ensembles/answers.md` | bagging vs boosting |
| [pa-ensemble](issues/10-pa-ensemble.md) | `learning/pa-ensemble/kNN_ensemble.py` | bagged `ScaledKNN` |
| [ra-streaming](issues/11-ra-streaming.md) | `learning/ra-streaming/answers.md` | batch vs stream |
| [ra-hardware](issues/12-ra-hardware.md) | `learning/ra-hardware/answers.md` | what to put on a GPU |
| [pa-gpu](issues/13-pa-gpu.md) | `learning/pa-gpu/knn_gpu.py` | array / GPU `leave_one_out` |
| [ra-drift](issues/14-ra-drift.md) | `learning/ra-drift/answers.md` | drift + prequential |
| [ra-imbalance](issues/15-ra-imbalance.md) | `learning/ra-imbalance/answers.md` | imbalance that moves |
| [ra-cost](issues/16-ra-cost.md) | `learning/ra-cost/answers.md` | weighted `vote` |
| [pa-online](issues/17-pa-online.md) | `learning/pa-online/online_knn.py` | window + `--weighted-vote` |
| [lr-jetson](issues/18-lr-jetson.md) | `learning/lr-jetson/AI_Jetson_Survey.md` | edge literature |
| [lr-slam](issues/19-lr-slam.md) | `learning/lr-slam/ROS_Jetson_SLAM.md` | SLAM vs classification |

```bash
task uv
task knn
task scaled NORMALIZE=zscore TASK=binary
task metrics
task selection
task ensemble
task gpu
task online
task online:weighted
task generate-stream
```

Do not use scikit-learn (or similar) to implement the classifier.

## Data

See `learning/resources/data/README.md`.

| File | Role |
| --- | --- |
| `small.arff` | default stationary set (Ecoli-style localization, 8 classes) |
| `medium.arff` | larger stationary set (white wine quality, 7 classes) |
| `large.arff` | stress / GPU comparison (same schema as `medium.arff`) |
| `small_stream.arff` | 800 instances, sudden drift at 400 (`pa-online`) |
| `medium_stream.arff` | 2000 instances, sudden drift at 1000 (`pa-online`) |

`learning/resources/generate_stream.py` rebuilds the stream files
(`task generate-stream`). Header comments document seed, drift index,
weights, and the label map.

## Using this as a GitHub template

1. Mark this repository as a template (Settings → Template repository).
2. Create a new repository from the template for the mentee. They are the owner.
3. They start at [git](issues/00-git.md), then [uv](issues/01-uv.md).
4. Recreate issues in the mentee repo with:

```bash
gh auth login
uv run scripts/create_issues.py
```

Issues are created in filename order, which matches the table.

## Mentors

Tickets are numbered procedures. After each PR, check that the new class
**subclasses** the previous one and did not paste a second distance function.
Common failures: query row in leave-one-out, scaler fit on the whole file,
accuracy-only reports, unscaled wine distances, copying `pa-knn` instead of
`import_pa`. Stretch goals are optional; do not block a PR that skipped
them. Do block a PR that broke the required class API in order to attempt
one.

Ask the student to add you as a collaborator (Write) and to run
`task github-rules` once so `main` cannot be updated except through a
reviewed PR.

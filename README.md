# ML Bootcamp

Template repository for a mentorship in applied machine learning classification.
Each student gets their own copy of this repo and owns it: the issues, the
branches, and the pull requests. Work happens under `learning/`. Shared data
and tooling live in `learning/resources/`.

kNN is the only algorithm you implement. Each programming assignment **imports
the previous class** and adds one facet. Fix a bug where you introduced it.

## Python and uv

Assignments are [uv](https://docs.astral.sh/uv/) **scripts**, not a project
venv. Each `learning/PA*/…py` file starts with a [PEP 723](https://peps.python.org/pep-0723/)
header. `uv run that_file.py` reads **that file's** `requires-python` and
`dependencies`. There is nothing to activate.

Install Python 3.10+ and uv in the Environment ticket (after PA0). Then:

```bash
uv run learning/ENV/hello.py
uv run learning/PA1/kNN.py learning/resources/data/small.arff
```

[Task](https://taskfile.dev/installation/) is optional sugar (`task pa1`
is the same `uv run`).

Third-party packages are declared in the file that uses them (matplotlib in
PA2/PA7; optional CuPy in PA4's header). Importing an earlier script does
**not** inherit its uv dependencies — re-list anything you still call.

## How code is reused

`learning/load_assignment.py` loads an earlier assignment as a module.

| You write | Class | Imports |
| --- | --- | --- |
| PA1 | `KNN` | — |
| PA6 | `ScaledKNN(KNN)` | PA1 |
| PA2 | `ReportingKNN(ScaledKNN)` | PA6 |
| PA7 | `SelectingKNN(ScaledKNN)` | PA6 + PA2 metrics |
| PA3 | `EnsembleKNN(ScaledKNN)` | PA6 + PA2 metrics |
| PA4 | `GpuKNN(ScaledKNN)` | PA6 + PA2 metrics |
| PA5 | `OnlineKNN(ScaledKNN)` | PA6 + PA2 metrics |

Do not copy `kNN.py` into the next folder. The skeletons already call
`import_pa('PA1')` (or PA6/PA2). Keep the class names.

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
  must not break PA6 importing PA1.

## Assignments

Do them in **table order**, not by assignment number. Numbers are stable IDs.

| Ticket | Path | You leave behind |
| --- | --- | --- |
| [PA0](issues/00-pa0-own-the-repo.md) | `learning/README.md` | owned repo, first PR |
| [ENV](issues/00b-env-python-uv.md) | `learning/ENV/` | uv + in-file deps |
| [RA1](issues/01-ra1-types-of-ml-problems.md) | `learning/RA1/answers.md` | problem types for these files |
| [PA1](issues/02-pa1-knn.md) | `learning/PA1/kNN.py` | class `KNN`, leave-one-out |
| [RA7](issues/03-ra7-feature-scaling.md) | `learning/RA7/answers.md` | why scale, how not to leak |
| [PA6](issues/04-pa6-scaling-and-task-types.md) | `learning/PA6/kNN_scaled.py` | `ScaledKNN`, `--normalize`, `--task` |
| [PA2](issues/05-pa2-metrics.md) | `learning/PA2/kNN_report.py` | `ReportingKNN`, baseline, plots |
| [RA8](issues/06-ra8-model-selection.md) | `learning/RA8/answers.md` | validation vs test |
| [PA7](issues/07-pa7-model-selection.md) | `learning/PA7/kNN_select.py` | `k` sweep, vote fractions |
| [RA2](issues/08-ra2-ensembles.md) | `learning/RA2/answers.md` | bagging vs boosting |
| [PA3](issues/09-pa3-knn-ensemble.md) | `learning/PA3/kNN_ensemble.py` | bagged `ScaledKNN` |
| [RA3](issues/10-ra3-data-flow.md) | `learning/RA3/answers.md` | batch vs stream |
| [RA4](issues/11-ra4-heterogeneous.md) | `learning/RA4/answers.md` | what to put on a GPU |
| [PA4](issues/12-pa4-gpu-knn.md) | `learning/PA4/knn_gpu.py` | array / GPU `leave_one_out` |
| [RA5](issues/13-ra5-concept-drift.md) | `learning/RA5/answers.md` | drift + prequential |
| [RA6](issues/14-ra6-class-imbalance.md) | `learning/RA6/answers.md` | imbalance that moves |
| [RA9](issues/15-ra9-cost-sensitive.md) | `learning/RA9/answers.md` | weighted `vote` |
| [PA5](issues/16-pa5-online-knn.md) | `learning/PA5/online_knn.py` | window + `--weighted-vote` |
| [LR1](issues/17-lr1-jetson-survey.md) | `learning/LR1/AI_Jetson_Survey.md` | edge literature |
| [LR2](issues/18-lr2-ros-slam.md) | `learning/LR2/ROS_Jetson_SLAM.md` | SLAM vs classification |

```bash
task env
task pa1
task pa6 NORMALIZE=zscore TASK=binary
task pa2
task pa7
task pa3
task pa4
task pa5
task pa5:weighted
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
| `small_stream.arff` | 800 instances, sudden drift at 400 (PA5) |
| `medium_stream.arff` | 2000 instances, sudden drift at 1000 (PA5) |

`learning/resources/generate_stream.py` rebuilds the stream files
(`task generate-stream`). Header comments document seed, drift index,
weights, and the label map.

## Using this as a GitHub template

1. Mark this repository as a template (Settings → Template repository).
2. Create a new repository from the template for the mentee. They are the owner.
3. They start at PA0, then ENV.
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
accuracy-only reports, unscaled wine distances, copying PA1 instead of
`import_pa`. Stretch goals are optional; do not block a PR that skipped
them. Do block a PR that broke the required class API in order to attempt
one.

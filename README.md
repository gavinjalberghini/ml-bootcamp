# ML Bootcamp

Template repository for a mentorship in applied machine learning classification.
Each student gets their own copy of this repo and owns it: the issues, the
branches, and the pull requests. Work happens under `learning/`. Shared data
and tooling live in `learning/resources/`.

kNN is the only algorithm you implement. Each assignment uses that one model
to open a different facet of classification: problem type, geometry, evaluation,
imbalance, model selection, ensembles, hardware, drift, and cost.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Task](https://taskfile.dev/installation/)
- Git and a GitHub account (see Programming Assignment 0)
- Python 3.10+ (installed automatically into a project environment by `uv`)

Windows users can work in native Python, WSL, or another Unix-like environment.
Nothing in the assignments requires WSL.

## Setup

```bash
task setup
```

That creates a virtual environment from `pyproject.toml` / `uv.lock`. Plotting
for PA2 comes from the base dependencies. GPU libraries for PA4 are opt-in:

```bash
task pa4:gpu
```

## Assignments

Tickets are also stored under `issues/` so they travel with the template.
Do them in the **table order below**, not by assignment number. PA/RA numbers
are stable IDs (PA5 is still the online kNN ticket), not week numbers. Later
programming assignments should reuse your earlier kNN code rather than
starting over.

| Ticket | Path | Facet |
| --- | --- | --- |
| [PA0](issues/00-pa0-own-the-repo.md) | `learning/README.md` | own the repo, branch, PR |
| [RA1](issues/01-ra1-types-of-ml-problems.md) | `learning/RA1/answers.md` | binary / multiclass / multilabel |
| [PA1](issues/02-pa1-knn.md) | `learning/PA1/kNN.py` | leave-one-out kNN, three distances |
| [RA7](issues/03-ra7-feature-scaling.md) | `learning/RA7/answers.md` | feature scale and distance geometry |
| [PA6](issues/04-pa6-scaling-and-task-types.md) | `learning/PA6/kNN_scaled.py` | normalization; binary vs multiclass |
| [PA2](issues/05-pa2-metrics.md) | `learning/PA2/kNN_report.py` | per-class metrics, baseline, plots |
| [RA8](issues/06-ra8-model-selection.md) | `learning/RA8/answers.md` | choosing `k`, validation vs test |
| [PA7](issues/07-pa7-model-selection.md) | `learning/PA7/kNN_select.py` | `k` sweep, vote-fraction confidence |
| [RA2](issues/08-ra2-ensembles.md) | `learning/RA2/answers.md` | bagging and boosting |
| [PA3](issues/09-pa3-knn-ensemble.md) | `learning/PA3/kNN_ensemble.py` | bootstrap ensemble; distance mix |
| [RA3](issues/10-ra3-data-flow.md) | `learning/RA3/answers.md` | batch vs streaming, sampling |
| [RA4](issues/11-ra4-heterogeneous.md) | `learning/RA4/answers.md` | CPU / GPU architectures |
| [PA4](issues/12-pa4-gpu-knn.md) | `learning/PA4/knn_gpu.py` | optional cupy (`--extra pa4-gpu`) |
| [RA5](issues/13-ra5-concept-drift.md) | `learning/RA5/answers.md` | concept drift |
| [RA6](issues/14-ra6-class-imbalance.md) | `learning/RA6/answers.md` | class imbalance in streams |
| [RA9](issues/15-ra9-cost-sensitive.md) | `learning/RA9/answers.md` | cost-sensitive and weighted votes |
| [PA5](issues/16-pa5-online-knn.md) | `learning/PA5/online_knn.py` | online kNN, window, weighted vote |
| [LR1](issues/17-lr1-jetson-survey.md) | `learning/LR1/AI_Jetson_Survey.md` | edge deployment literature |
| [LR2](issues/18-lr2-ros-slam.md) | `learning/LR2/ROS_Jetson_SLAM.md` | robotics literature |

Programming assignments are stdlib-only except PA2 (matplotlib, already in the
project) and PA4's optional GPU extra. Do not use scikit-learn or similar ML
libraries to implement the classifier.

```bash
task pa1
task pa1 DATA=learning/resources/data/medium.arff K=5
task pa6 NORMALIZE=zscore TASK=binary
task pa7
task pa4:gpu
task pa5
task pa5:weighted
task generate-stream
```

Each `task paN` runs the skeleton or your implementation in `learning/PAN/`.
Fill in the TODOs; do not replace the command-line contract the Taskfile uses.

## Data

Files in `learning/resources/data/` (see that folder's README for schemas,
class meanings, and imbalance notes):

| File | Role |
| --- | --- |
| `small.arff` | default stationary set (Ecoli-style localization, 8 classes) |
| `medium.arff` | larger stationary set (white wine quality, 7 classes) |
| `large.arff` | stress / GPU comparison (same schema as `medium.arff`) |
| `small_stream.arff` | 800 instances, sudden drift at 400 (PA5) |
| `medium_stream.arff` | 2000 instances, sudden drift at 1000 (PA5) |

`learning/resources/generate_stream.py` rebuilds the stream files from the
stationary ARFFs (`task generate-stream`). Header comments on each stream file
document the seed, drift index, class weights, and label map.

## Using this as a GitHub template

1. On GitHub, mark this repository as a template (Settings → Template repository).
2. Create a new repository from the template for the mentee. They are the owner.
3. The mentee clones *their* repo and starts at PA0.
4. Recreate the assignment issues from `issues/` in the mentee repo with:

```bash
gh auth login
python3 scripts/create_issues.py
```

Issues are created in filename order, which matches the table above.
The script will not close or update issues that already exist; it only creates
new ones.

## Mentors

Teaching is still conversation. The tickets are contracts (paths, CLI, outputs,
questions), not lectures. After each assignment, look at the "as you work"
questions in the issue and the student's markdown. Common failure modes to
watch for: including the query row in leave-one-out, fitting a scaler on the
whole file, reporting only accuracy on these imbalanced sets, and treating
`medium.arff` distances as meaningful before PA6.

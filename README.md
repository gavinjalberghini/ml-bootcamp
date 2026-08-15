# ML Bootcamp

Template repository for a mentorship sequence in applied machine learning.
Students implement each assignment from the GitHub issues (also stored under
`issues/` so the tickets travel with the template).

Work goes in `learning/<your_name>/`. Shared data and tooling live in
`learning/resources/`.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Task](https://taskfile.dev/installation/)
- Git and a GitHub account (see Programming Assignment 0)

## Setup

```bash
task setup
```

## Assignments

| Ticket | Path | Notes |
| --- | --- | --- |
| [PA0](issues/00-pa0-git-learning.md) | `learning/<your_name>/README.md` | git clone, branch, PR |
| [RA1](issues/01-ra1-types-of-ml-problems.md) | `learning/<your_name>/RA1/answers.md` | classification types |
| [PA1](issues/02-pa1-knn.md) | `learning/<your_name>/PA1/kNN.py` | stdlib kNN, three distances |
| [RA2](issues/03-ra2-ensembles.md) | `learning/<your_name>/RA2/answers.md` | bagging and boosting |
| [PA2](issues/04-pa2-visualizing.md) | `learning/<your_name>/PA2/` | per-class metrics, time, memory |
| [RA3](issues/05-ra3-data-flow.md) | `learning/<your_name>/RA3/answers.md` | batch vs streaming, sampling |
| [PA3](issues/06-pa3-knn-ensemble.md) | `learning/<your_name>/PA3/kNN_ensemble.py` | three kNNs, majority vote |
| [RA4](issues/07-ra4-heterogeneous.md) | `learning/<your_name>/RA4/answers.md` | CPU/GPU architectures |
| [PA4](issues/08-pa4-gpu-knn.md) | `learning/<your_name>/PA4/knn_gpu.py` | optional cupy (`--extra pa4-gpu`) |
| [RA5](issues/09-ra5-concept-drift.md) | `learning/<your_name>/RA5/answers.md` | concept drift |
| [RA6](issues/10-ra6-class-imbalance.md) | `learning/<your_name>/RA6/answers.md` | class imbalance in streams |
| [PA5](issues/11-pa5-online-knn.md) | `learning/<your_name>/PA5/online_knn.py` | online kNN, sliding window |
| [LR1](issues/12-lr1-jetson-survey.md) | `learning/<your_name>/LR1/AI_Jetson_Survey.md` | literature review |
| [LR2](issues/13-lr2-ros-slam.md) | `learning/<your_name>/LR2/ROS_Jetson_SLAM.md` | literature review |

Programming assignments are stdlib-only except PA4's optional GPU extra.

```bash
task pa1 STUDENT=your_name
task pa1 STUDENT=your_name DATA=learning/resources/data/medium.arff K=5
task pa4:gpu STUDENT=your_name
task generate-stream
```

## Data

Files in `learning/resources/data/`:

| File | Role |
| --- | --- |
| `small.arff` | default stationary set (PA1–PA4) |
| `medium.arff` | larger stationary set |
| `large.arff` | stress / GPU comparison |
| `small_stream.arff` | 800 instances, sudden drift at 400 (PA5) |
| `medium_stream.arff` | 2000 instances, sudden drift at 1000 (PA5) |

`learning/resources/generate_stream.py` rebuilds the stream files from the
stationary ARFFs (`task generate-stream`). Header comments on each stream file
document the seed, drift index, class weights, and label map.

## Using this as a GitHub template

1. On GitHub, mark this repository as a template (Settings → Template repository).
2. Use it to start a new mentee repo.
3. Recreate the assignment issues from `issues/` with:

```bash
gh auth login
python3 scripts/create_issues.py
```

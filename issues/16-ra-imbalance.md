# [ra-imbalance] Class Imbalance in Data Streams

You need: pa-metrics (you have already seen accuracy hide rare classes on
`small.arff`). ra-drift answered.

You will: move from static imbalance to imbalance that **changes** after
drift. pa-online will report per-class metrics over time. ra-cost will add weighted
votes.

## Steps

1. Open your pa-metrics `output_report.md` and the pre/post weights in
   `small_stream.arff`.
2. Read [imbalanced classes](https://www.geeksforgeeks.org/machine-learning/how-to-handle-imbalanced-classes-in-machine-learning/).
3. Read [Google ML Crash Course — imbalanced datasets](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets).
4. Read [a gentle introduction to imbalanced classification](https://machinelearningmastery.com/what-is-imbalanced-classification/).
5. Answer every heading in `learning/ra-imbalance/answers.md`:
   - Why high accuracy can still mean failure (use pa-metrics or `small.arff`)
   - Oversampling vs undersampling vs cost-sensitive learning
   - Why a fixed class-ratio method goes stale on a stream
   - How drift and imbalance interact (use the stream header weights)
   - How imbalance affects kNN votes; what window or sampling changes help
6. Commit and open a PR.

## What to turn in

- Filled `learning/ra-imbalance/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- One answer quotes or paraphrases the pre- and post-drift weights.
- Stretch is optional. Skipping it does not block ra-cost.

## Stretch goal (optional)

**Challenge:** In `learning/ra-imbalance/answers.md` under “Stretch goal”, propose a
window-only resample idea (what you would drop or repeat, and why it goes
stale after the label map). No code.

## Optional research

- [2204.03719](https://arxiv.org/abs/2204.03719)

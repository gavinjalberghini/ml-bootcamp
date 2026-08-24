# [Reading Assignment 6] Class Imbalance in Data Streams

You need: PA2 (you have already seen accuracy hide rare classes on
`small.arff`). RA5 answered.

You will: move from static imbalance to imbalance that **changes** after
drift. PA5 will report per-class metrics over time. RA9 will add weighted
votes.

## Steps

1. Open your PA2 `output_report.md` and the pre/post weights in
   `small_stream.arff`.
2. Read [imbalanced classes](https://www.geeksforgeeks.org/machine-learning/how-to-handle-imbalanced-classes-in-machine-learning/).
3. Read [Google ML Crash Course — imbalanced datasets](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets).
4. Read [a gentle introduction to imbalanced classification](https://machinelearningmastery.com/what-is-imbalanced-classification/).
5. Answer every heading in `learning/RA6/answers.md`:
   - Why high accuracy can still mean failure (use PA2 or `small.arff`)
   - Oversampling vs undersampling vs cost-sensitive learning
   - Why a fixed class-ratio method goes stale on a stream
   - How drift and imbalance interact (use the stream header weights)
   - How imbalance affects kNN votes; what window or sampling changes help
6. Commit and open a PR.

## What to turn in

- Filled `learning/RA6/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- One answer quotes or paraphrases the pre- and post-drift weights.

## Optional research

- [2204.03719](https://arxiv.org/abs/2204.03719)

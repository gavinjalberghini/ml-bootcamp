# [ra-cost] Cost-Sensitive Classification

You need: ra-imbalance and pa-metrics. pa-selection already produced vote fractions.

You will: decide how to change **`vote`**, not the distance math. pa-online will
add `--weighted-vote` on the class you already have.

## Steps

1. Read [cost-sensitive learning](https://en.wikipedia.org/wiki/Cost-sensitive_learning).
2. Read [cost-sensitive learning for imbalanced classification](https://machinelearningmastery.com/cost-sensitive-learning-for-imbalanced-classification/).
3. Read [class weights vs resampling](https://www.analyticsvidhya.com/blog/2020/10/improve-class-imbalance-class-weights/).
4. Re-read your ra-imbalance answers on streams.
5. Answer every heading in `learning/ra-cost/answers.md`:
   - Cost matrix vs resampling
   - Inverse-frequency weighting vs macro-F1 / balanced accuracy
   - What goes wrong with 1/count for a class seen once, or after a
     majority/minority swap
   - When to threshold pa-selection vote fractions instead of changing weights
   - Which mistakes on `small.arff` you would cost higher, and why
6. Commit and open a PR.

## What to turn in

- Filled `learning/ra-cost/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- You describe the `--weighted-vote` rule pa-online will implement: weight a
  neighbor by the inverse of its class count **in the current window**.
- Stretch is optional. Skipping it does not block pa-online.

## Stretch goal (optional)

**Challenge:** Invent a 2×2 cost matrix for wine `low` vs `high` (binary
task from pa-scaled) in `learning/ra-cost/answers.md` under “Stretch goal”. Do not
require pa-online to read that matrix.

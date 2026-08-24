# [Reading Assignment 9] Cost-Sensitive Classification

You need: RA6 and PA2. PA7 already produced vote fractions.

You will: decide how to change **`vote`**, not the distance math. PA5 will
add `--weighted-vote` on the class you already have.

## Steps

1. Read [cost-sensitive learning](https://en.wikipedia.org/wiki/Cost-sensitive_learning).
2. Read [cost-sensitive learning for imbalanced classification](https://machinelearningmastery.com/cost-sensitive-learning-for-imbalanced-classification/).
3. Read [class weights vs resampling](https://www.analyticsvidhya.com/blog/2020/10/improve-class-imbalance-class-weights/).
4. Re-read your RA6 answers on streams.
5. Answer every heading in `learning/RA9/answers.md`:
   - Cost matrix vs resampling
   - Inverse-frequency weighting vs macro-F1 / balanced accuracy
   - What goes wrong with 1/count for a class seen once, or after a
     majority/minority swap
   - When to threshold PA7 vote fractions instead of changing weights
   - Which mistakes on `small.arff` you would cost higher, and why
6. Commit and open a PR.

## What to turn in

- Filled `learning/RA9/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- You describe the `--weighted-vote` rule PA5 will implement: weight a
  neighbor by the inverse of its class count **in the current window**.
- Stretch is optional. Skipping it does not block PA5.

## Stretch goal (optional)

**Challenge:** Invent a 2×2 cost matrix for wine `low` vs `high` (binary
task from PA6) in `learning/RA9/answers.md` under “Stretch goal”. Do not
require PA5 to read that matrix.

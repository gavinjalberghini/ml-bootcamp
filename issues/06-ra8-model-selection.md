# [Reading Assignment 8] Model Selection and Validation

You need: PA2 done. You can report macro-F1. You have been using a single
`k` (often 3).

You will: learn why you must not pick `k` on the same number you publish.
PA7 will hold out 20% of the rows, choose `k` on the rest, and score the
held-out slice.

## Steps

1. Read [training, validation, and test sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets).
2. Read [cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)).
3. Read [bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff).
4. Read [hyperparameter optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization).
5. Skim [choosing k](https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/).
6. Answer every heading in `learning/RA8/answers.md`:
   - Training vs validation vs test; where leave-one-out sits
   - Why “best LOO `k`, report that LOO score” is optimistic
   - Nested validation vs a single holdout
   - How accuracy and macro-F1 should move as `k` grows on `small.arff`
   - What vote fractions tell you that a hard label does not
7. Commit and open a PR.

## What to turn in

- Filled `learning/RA8/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- You describe the 80/20 split PA7 will use, in your own words.
- Stretch is optional. Skipping it does not block PA7.

## Stretch goal (optional)

**Challenge:** In `learning/RA8/answers.md` under “Stretch goal”, sketch
nested validation in words (outer split for the number you publish, inner
split for choosing `k`). No code. PA7 stays a single holdout.

# [Reading Assignment 8] Model Selection and Validation

`k` is not a detail. Small `k` follows local noise; large `k` smooths toward
the majority class. Distance choice and normalization are also model decisions.
If you try several settings and then report the best leave-one-out score from
the same pass, you have used the evaluation set to pick the model.

This reading is about that split: what you may look at while choosing `k`,
and what you may report as the final number.

As you read, think about the following:

- What is the difference between a training set, a validation set, and a
  test set? Where does leave-one-out sit in that picture?
- Why is “pick the `k` with the best LOO accuracy, then report that
  accuracy” optimistic?
- How does nested validation differ from a single holdout?
- For kNN specifically, how do you expect accuracy and macro-F1 to move as
  `k` grows on an imbalanced file like `small.arff`?
- What would a vote fraction (4 of 5 neighbors agree vs 3 of 5) tell you
  that a hard label does not?

You will implement a `k` sweep and vote-fraction confidence in PA7.

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA8/answers.md`.

## Articles

- [Training, validation, and test sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets)
- [Cross-validation (Wikipedia)](https://en.wikipedia.org/wiki/Cross-validation_(statistics))
- [Bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
- [Hyperparameter optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization)
- [Choosing k in kNN (Machine Learning Mastery)](https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/)

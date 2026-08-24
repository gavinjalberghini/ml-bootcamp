# [Reading Assignment 9] Cost-Sensitive Classification

Accuracy treats every mistake as equal. In many classification problems they
are not: missing a rare localization site, or calling a bad wine excellent,
is worse than the reverse. Cost-sensitive learning builds that asymmetry
into the decision.

For kNN the usual hook is the **vote**. Uniform majority vote is implicit
equal cost. You can weight neighbors by inverse class frequency, by a cost
matrix, or by distance. In a stream those weights should be allowed to move,
because RA6's imbalance ratio is not fixed.

As you read, think about the following:

- What is a cost matrix, and how does it differ from resampling the data?
- How is inverse-frequency weighting related to balanced accuracy or
  macro-F1?
- If you weight kNN votes by 1 / class_count in the current window, what
  happens to a brand-new class that has been seen once? What happens after
  a drift that swaps majority and minority?
- When would you rather change the decision threshold on vote fractions
  (PA7) than change the neighbor weights?
- Which mistakes on `small.arff` would you assign a higher cost, and why?

PA5 asks for an optional `--weighted-vote` that uses inverse class frequency
in the current window.

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA9/answers.md`.

## Articles

- [Cost-sensitive learning (Wikipedia)](https://en.wikipedia.org/wiki/Cost-sensitive_learning)
- [Cost-sensitive learning overview](https://machinelearningmastery.com/cost-sensitive-learning-for-imbalanced-classification/)
- [Class weights vs resampling](https://www.analyticsvidhya.com/blog/2020/10/improve-class-imbalance-class-weights/)
- RA6 (re-read the stream interaction questions)

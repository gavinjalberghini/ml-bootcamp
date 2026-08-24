# [Reading Assignment 7] Feature Scaling and Distance Geometry

kNN is a geometric classifier. The “nearest” neighbor is defined by a distance
on the feature vector, so the units and spreads of the columns *are* the
model. If one column ranges from 0 to 300 and another from 0 to 1, Euclidean
distance is almost entirely the first column.

You did not scale in PA1. On `small.arff` the features are already on similar
numeric ranges. On `medium.arff` they are not (see
`learning/resources/data/README.md`). This reading is about why that matters
and how to fix it without leaking.

As you read, think about the following:

- Why do min-max scaling and z-score standardization change kNN neighbors
  when they would not change a tree split on a single feature?
- When would you prefer z-score over min-max, or the reverse?
- If you compute mean and standard deviation on the entire ARFF file and then
  do leave-one-out, what information has leaked into each query?
- How should a scaler be fit under leave-one-out? Under a train/validation
  split?
- Looking at the wine features, which columns do you expect to dominate
  unscaled Euclidean distance?

You will implement `--normalize` in PA6.

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA7/answers.md`.

## Articles

- [Feature scaling (Wikipedia)](https://en.wikipedia.org/wiki/Feature_scaling)
- [Normalization vs standardization](https://www.geeksforgeeks.org/normalization-vs-standardization/)
- [Why kNN needs feature scaling](https://stats.stackexchange.com/questions/287425/why-do-you-need-to-scale-data-in-knn)
- [Data leakage in preprocessing (scikit-learn)](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage-during-pre-processing) — read the idea; do not use the library

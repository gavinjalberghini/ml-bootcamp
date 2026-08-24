# [Reading Assignment 7] Feature Scaling and Distance Geometry

You need: PA1 done. You have a `KNN` class that does not scale features.

You will: understand why that class is already fair on `small.arff` and
unfair on `medium.arff`, and how to scale **without leaking** the query
into the scaler. PA6 will add `--normalize` to the same class.

## Steps

1. Re-read the wine feature ranges in `learning/resources/data/README.md`.
2. Read [feature scaling](https://en.wikipedia.org/wiki/Feature_scaling).
3. Read [normalization vs standardization](https://www.geeksforgeeks.org/normalization-vs-standardization/).
4. Read [why kNN needs scaling](https://stats.stackexchange.com/questions/287425/why-do-you-need-to-scale-data-in-knn).
5. Read the leakage section of [scikit-learn's preprocessing pitfalls](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage-during-pre-processing).
   You will not use that library.
6. Answer every heading in `learning/RA7/answers.md`:
   - Why do min-max and z-score change kNN neighbors when they would not
     change a single-feature tree split?
   - When would you prefer z-score over min-max, or the reverse?
   - If you fit a scaler on the entire file and then do leave-one-out, what
     leaked?
   - How should a scaler be fit under leave-one-out? Under a train/validation
     split?
   - Which wine columns do you expect to dominate unscaled Euclidean
     distance?
7. Commit and open a PR.

## What to turn in

- Filled `learning/RA7/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- At least one answer names a wine column and the leave-one-out leakage
  rule PA6 will have to follow.

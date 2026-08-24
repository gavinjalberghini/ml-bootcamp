# [Programming Assignment 1] Implement kNN on Stationary Data

kNN is the model you will carry through the rest of this mentorship. In this
ticket you implement a multiclass kNN yourself and evaluate it with a protocol
that does not leak the query point into its own neighbor set.

**Do not use ML libraries** (no scikit-learn, no TensorFlow, no kNN from a
package). Stdlib only. Online references are allowed. **GAI should not write
the implementation for you;** use it only when you are stuck on a specific
error.

A skeleton lives at `learning/PA1/kNN.py`. Keep its command-line flags; fill
in the TODOs.

## 1. The algorithm

Read an ARFF file from the command line. The last column is the class label;
drop it before you compute distance. Implement three distances and select one
with `--distance`:

1. Euclidean
2. Manhattan
3. Minkowski (exponent `--p`, default 3)

Evaluate with **leave-one-out**. For each row `i`:

1. Treat row `i` as the query. Do not put it in the neighbor pool.
2. Find the `k` nearest remaining rows under the chosen distance.
3. Predict the majority class among those neighbors. Define a deterministic
   tie-break (for example: nearest neighbor among the tied classes, then
   lowest class id).
4. Compare the prediction to the true label of row `i`.

Do not train on the full file and then score the same rows. That is leakage,
and the accuracy will be dishonest.

Write elapsed time, the selected distance, `k`, the data path, and the full
confusion matrix to `learning/PA1/output_knn.md` (override with `--output`).

Run `task pa1` against `learning/resources/data/small.arff`. Also run once
against `medium.arff` so you have a feel for cost; you do not need a perfect
report on the large wine set yet.

## 2. The data

ARFF headers describe the attributes. See `learning/resources/data/README.md`
for what `small.arff` and `medium.arff` actually are (Ecoli localization and
white wine quality). Class codes are categories. `small.arff` has eight
classes and is already imbalanced; a 40%+ accuracy can be a majority guess.

Do not scale features in this ticket. You will see why that matters in RA7
and PA6.

## Acceptance criteria

- `learning/PA1/kNN.py` runs via `task pa1` and via
  `task pa1 DATA=learning/resources/data/medium.arff K=5`.
- Leave-one-out is implemented as specified. The query row is excluded.
- `--distance` selects Euclidean, Manhattan, or Minkowski.
- `learning/PA1/output_knn.md` contains settings, elapsed time, and a
  confusion matrix whose rows and columns are labeled with class ids.

## References

- [k-nearest neighbors, overview](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
- [Distance metrics for kNN](https://www.kdnuggets.com/2020/11/most-popular-distance-metrics-knn.html)
- [Multiclass confusion matrix](https://www.analyticsvidhya.com/blog/2021/06/confusion-matrix-for-multi-class-classification/)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [ARFF](https://waikato.github.io/weka-wiki/formats_and_processing/arff/)
- [Python tutorial](https://docs.python.org/3/tutorial/)

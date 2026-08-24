# [Programming Assignment 2] Metrics, Baselines, and Visualizations

A confusion matrix is not enough. These datasets are imbalanced, so a high
accuracy can still mean the model never finds a rare class. This ticket turns
your kNN into a report you can trust, and it forces a comparison against a
classifier that does not look at the features at all.

Copy forward your scaled kNN (PA6) or PA1 if you must. A skeleton lives at
`learning/PA2/kNN_report.py`. Keep `--distance`, `--k`, `--p`, and
`--normalize`. **Stdlib plus matplotlib only. GAI should not implement this
for you.**

## What to compute

Evaluate with the same leave-one-out protocol as PA1/PA6. Then report:

**Majority-class baseline.** Ignore the features. Always predict the most
frequent class in the file (for leave-one-out you may use the class
distribution of the neighbor pool so the baseline also excludes the query).
Give the baseline its own accuracy and confusion matrix. If kNN does not beat
this, the interesting story is why.

**Overall**

- Accuracy
- Macro-averaged precision, recall, and F1
- Weighted-averaged precision, recall, and F1

**Per class** (every class that appears in the file)

- Precision, recall, F1
- Support (how many true instances)
- Sensitivity (same as recall)
- Specificity (TN / (TN + FP) in the one-vs-rest view of that class)

Define precision and recall from the confusion matrix. If a class has zero
predicted positives, precision is 0, not undefined — state that choice.

**Resources**

- Wall-clock time for the evaluation
- Peak memory of the Python process

**Plots** (matplotlib; write image files next to the report)

- Confusion matrix as a labeled heatmap or table figure
- Per-class F1 bar chart, including the majority baseline's per-class F1
  if you computed it

Do not hide the rare classes. On `small.arff`, classes 2, 3, and 6 will look
bad; that is the point.

## Outputs

Write `learning/PA2/output_report.md` (`--output`) with settings, baseline
metrics, kNN metrics, and paths to the figures. Run:

```bash
task pa2
task pa2 DATA=learning/resources/data/medium.arff NORMALIZE=zscore
```

In a short closing section, answer:

- How much of PA1's accuracy on `small.arff` was the majority class?
- Why can accuracy and macro-F1 disagree here?
- Did z-score on `medium.arff` move macro-F1 more than accuracy?

## Acceptance criteria

- `learning/PA2/kNN_report.py` runs via `task pa2`.
- The report includes the majority baseline, overall and per-class metrics,
  time, memory, and at least the two figures above.
- Macro vs weighted averages are labeled as such.

## References

- [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall)
- [F-score](https://en.wikipedia.org/wiki/F-score)
- [Macro vs weighted averages](https://www.geeksforgeeks.org/machine-learning/macro-average-and-weighted-average-in-classification/)
- [Memory of a Python process](https://docs.python.org/3/library/resource.html) (`resource.getrusage`) or `/proc/self/status` on Linux
- [matplotlib tutorials](https://matplotlib.org/stable/tutorials/pyplot.html)

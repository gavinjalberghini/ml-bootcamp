# [pa-metrics] Metrics, Baselines, and Visualizations

You need: pa-scaled done (`ScaledKNN` imports pa-knn). You already have confusion
matrices. These files are imbalanced; accuracy alone is not enough.

You will: subclass `ScaledKNN`, add a majority baseline and real metrics,
and plot them. **GAI should not implement this for you.**

matplotlib is listed in this file's `# /// script` dependencies. `uv run`
installs it for this script only. Do not `pip install` it yourself.

## Steps

1. Open `learning/pa-metrics/kNN_report.py`. Keep `import_pa('pa-scaled')` and
   `class ReportingKNN(scaled.ScaledKNN)`. Confirm the script header lists
   `matplotlib>=3.8`. Required methods have sudo comments.
2. Implement `majority_baseline(labels)`. Ignore features. For each row,
   predict the most frequent class in the *other* rows (leave-one-out
   majority) or, if you document it, the global majority. Return
   `(y_true, y_pred)`.
3. Implement `metrics_report(y_true, y_pred)` from the confusion matrix.
   Return a dict that includes at least `accuracy`, `macro_f1`,
   `weighted_f1`, and a per-class structure with precision, recall, F1,
   support, sensitivity (recall), and specificity
   (`TN/(TN+FP)` one-vs-rest). Later tickets read `macro_f1`. If a class
   has zero predicted positives, precision is 0. State that.
4. Implement `peak_memory_bytes` (`resource.getrusage` or
   `/proc/self/status` on Linux).
5. Implement `write_figures`: a labeled confusion heatmap and a per-class
   F1 bar chart that includes the baseline's per-class F1. Save images next
   to the report. Do not drop rare classes.
6. `leave_one_out` comes from pa-scaled/pa-knn. Call it; do not rewrite neighbor
   search here.
7. Run:

   ```bash
   task metrics
   task metrics DATA=learning/resources/data/medium.arff NORMALIZE=zscore
   ```

8. In `learning/pa-metrics/output_report.md` answer:
   - How much of pa-knn's accuracy on `small.arff` was the majority class?
   - Why can accuracy and macro-F1 disagree here?
   - Did z-score on `medium.arff` move macro-F1 more than accuracy?
9. Commit and open a PR.

## Command-line contract

`data`, `--distance`, `--k`, `--p`, `--normalize`, `--output` (default
`output_report.md`).

## What to turn in

- `learning/pa-metrics/kNN_report.py`
- `output_report.md`, figure files, and the three answers above

## Acceptance criteria

- `ReportingKNN` subclasses `ScaledKNN`. Metrics and plots are new; distance
  is not rewritten.
- The report includes baseline vs kNN, macro vs weighted, time, and memory.
- `uv run learning/pa-metrics/kNN_report.py …` installs matplotlib from the script
  header.
- Stretch is optional. Skipping `stretch_metric_interval` does not block pa-selection.

## Stretch goal (optional)

Later tickets only call `metrics_report`. They never call the stretch
method.

**Challenge:** Put an uncertainty idea on `stretch_metric_interval` (for
example a resampled range around macro-F1) and write
`learning/pa-metrics/stretch.md`. Do not change the keys `metrics_report` must
already return.

## References

- [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall)
- [F-score](https://en.wikipedia.org/wiki/F-score)
- [Macro vs weighted averages](https://www.geeksforgeeks.org/machine-learning/macro-average-and-weighted-average-in-classification/)
- [matplotlib pyplot](https://matplotlib.org/stable/tutorials/pyplot.html)

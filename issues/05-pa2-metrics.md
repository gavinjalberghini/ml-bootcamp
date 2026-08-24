# [Programming Assignment 2] Metrics, Baselines, and Visualizations

You need: PA6 done (`ScaledKNN` imports PA1). You already have confusion
matrices. These files are imbalanced; accuracy alone is not enough.

You will: subclass `ScaledKNN`, add a majority baseline and real metrics,
and plot them. **GAI should not implement this for you.**

matplotlib is listed in this file's `# /// script` dependencies. `uv run`
installs it for this script only. Do not `pip install` it yourself.

## Steps

1. Open `learning/PA2/kNN_report.py`. Keep `import_pa('PA6')` and
   `class ReportingKNN(PA6.ScaledKNN)`. Confirm the script header lists
   `matplotlib>=3.8`.
2. Implement `majority_baseline(labels)`. Ignore features. For each row,
   predict the most frequent class in the *other* rows (leave-one-out
   majority) or, if you document it, the global majority. Return
   `(y_true, y_pred)`.
3. Implement `metrics_report(y_true, y_pred)` from the confusion matrix:
   - overall accuracy
   - macro-averaged precision, recall, F1
   - weighted-averaged precision, recall, F1
   - per class: precision, recall, F1, support, sensitivity (recall),
     specificity (TN/(TN+FP) in that class's one-vs-rest view)
   If a class has zero predicted positives, precision is 0. State that.
4. Implement `peak_memory_bytes` (`resource.getrusage` or
   `/proc/self/status` on Linux).
5. Implement `write_figures`: a labeled confusion heatmap and a per-class
   F1 bar chart that includes the baseline's per-class F1. Save images next
   to the report. Do not drop rare classes.
6. `leave_one_out` comes from PA6/PA1. Call it; do not rewrite neighbor
   search here.
7. Run:

   ```bash
   task pa2
   task pa2 DATA=learning/resources/data/medium.arff NORMALIZE=zscore
   ```

8. In `learning/PA2/output_report.md` answer:
   - How much of PA1's accuracy on `small.arff` was the majority class?
   - Why can accuracy and macro-F1 disagree here?
   - Did z-score on `medium.arff` move macro-F1 more than accuracy?
9. Commit and open a PR.

## Command-line contract

`data`, `--distance`, `--k`, `--p`, `--normalize`, `--output` (default
`output_report.md`).

## What to turn in

- `learning/PA2/kNN_report.py`
- `output_report.md`, figure files, and the three answers above

## Acceptance criteria

- `ReportingKNN` subclasses `ScaledKNN`. Metrics and plots are new; distance
  is not rewritten.
- The report includes baseline vs kNN, macro vs weighted, time, and memory.
- `uv run learning/PA2/kNN_report.py …` installs matplotlib from the script
  header.

## References

- [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall)
- [F-score](https://en.wikipedia.org/wiki/F-score)
- [Macro vs weighted averages](https://www.geeksforgeeks.org/machine-learning/macro-average-and-weighted-average-in-classification/)
- [matplotlib pyplot](https://matplotlib.org/stable/tutorials/pyplot.html)

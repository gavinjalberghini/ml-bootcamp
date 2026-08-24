# [pa-selection] Choosing k and Soft Predictions

You need: pa-scaled (`ScaledKNN`) and pa-metrics (`ReportingKNN.metrics_report`). ra-selection
answered.

You will: import those modules, hold out 20% of the rows, pick `k` on the
other 80%, and report vote fractions on the test slice. Do not copy pa-knn/pa-scaled
distance code. **GAI should not implement this for you.**

This file's script header lists matplotlib because you will plot macro-F1
vs `k`. Importing pa-metrics does not install matplotlib for you.

## Steps

1. Open `learning/pa-selection/kNN_select.py`. Keep `import_pa('pa-scaled')` and
   `import_pa('pa-metrics')`. `SelectingKNN` subclasses `ScaledKNN`. Required
   methods have sudo comments.
2. Implement `split(features, labels, seed, test_frac=0.2)`. Shuffle with
   that seed. Return `train_x, train_y, test_x, test_y`.
3. For each `k` in `--k-grid` (default `1,3,5,7,9`), run **leave-one-out
   on the 80% only** using `SelectingKNN(k=..., normalize=...)`. Score with
   `ReportingKNN.metrics_report`. Record accuracy and macro-F1.
4. Choose the `k` with the best **macro-F1** on that 80%. Tie-break: smaller
   `k`.
5. Implement `predict_with_votes(query, pool_x, pool_y)`. Use the 80% as
   the pool (not leave-one-out on the test row). Return
   `(predicted_label, votes_for_winner / k)`. Scaling still fits on the
   pool only (pa-scaled).
6. Score the 20% test set with the chosen `k`. Also score the majority
   baseline on the test set using the majority label of the 80% (use pa-metrics).
7. Write `learning/pa-selection/output_select.md` plus a plot of validation macro-F1
   vs `k`. Include mean vote fraction on correct vs incorrect test
   predictions, and a table of test errors (true, pred, vote fraction).
8. Run:

   ```bash
   task selection
   task selection DATA=learning/resources/data/medium.arff NORMALIZE=zscore
   ```

9. In the markdown answer:
   - Which `k` won on each file, and did test macro-F1 match the validation
     ranking?
   - What happens to rare-class recall as `k` grows?
   - Would you ship the validation `k`, or do you want a nested scheme?
10. Commit and open a PR.

## Command-line contract

`data`, `--k-grid`, `--distance`, `--p`, `--normalize`, `--seed` (default 5),
`--output` (default `output_select.md`).

## What to turn in

- `learning/pa-selection/kNN_select.py`
- `output_select.md`, the F1-vs-`k` figure, and the three answers

## Acceptance criteria

- Headline metrics are from the 20% test slice. `k` was chosen on the 80%.
- Distance and scaling come from pa-scaled; metrics come from pa-metrics.
- Vote fractions appear in the report.
- Stretch is optional. Skipping `stretch_brier` does not block pa-ensemble.

## Stretch goal (optional)

**Challenge:** Score the test slice with a Brier-style number on
`stretch_brier` and record it in `learning/pa-selection/stretch.md`. Do not make
`task selection` fail if that method is still unimplemented.

## References

- ra-selection
- [Brier score](https://en.wikipedia.org/wiki/Brier_score) (optional extra)

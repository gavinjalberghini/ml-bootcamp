# [Programming Assignment 7] Choosing k and Soft Predictions

You need: PA6 (`ScaledKNN`) and PA2 (`ReportingKNN.metrics_report`). RA8
answered.

You will: import those modules, hold out 20% of the rows, pick `k` on the
other 80%, and report vote fractions on the test slice. Do not copy PA1/PA6
distance code. **GAI should not implement this for you.**

This file's script header lists matplotlib because you will plot macro-F1
vs `k`. Importing PA2 does not install matplotlib for you.

## Steps

1. Open `learning/PA7/kNN_select.py`. Keep `import_pa('PA6')` and
   `import_pa('PA2')`. `SelectingKNN` subclasses `ScaledKNN`. Required
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
   pool only (PA6).
6. Score the 20% test set with the chosen `k`. Also score the majority
   baseline on the test set using the majority label of the 80% (use PA2).
7. Write `learning/PA7/output_select.md` plus a plot of validation macro-F1
   vs `k`. Include mean vote fraction on correct vs incorrect test
   predictions, and a table of test errors (true, pred, vote fraction).
8. Run:

   ```bash
   task pa7
   task pa7 DATA=learning/resources/data/medium.arff NORMALIZE=zscore
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

- `learning/PA7/kNN_select.py`
- `output_select.md`, the F1-vs-`k` figure, and the three answers

## Acceptance criteria

- Headline metrics are from the 20% test slice. `k` was chosen on the 80%.
- Distance and scaling come from PA6; metrics come from PA2.
- Vote fractions appear in the report.
- Stretch is optional. Skipping `stretch_brier` does not block PA3.

## Stretch goal (optional)

**Challenge:** Score the test slice with a Brier-style number on
`stretch_brier` and record it in `learning/PA7/stretch.md`. Do not make
`task pa7` fail if that method is still unimplemented.

## References

- RA8
- [Brier score](https://en.wikipedia.org/wiki/Brier_score) (optional extra)

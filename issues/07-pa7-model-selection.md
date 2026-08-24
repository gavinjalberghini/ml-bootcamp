# [Programming Assignment 7] Choosing k and Soft Predictions

You now have metrics (PA2) and a reason not to tune on the number you report
(RA8). This ticket makes `k` a search, and it records how sure the neighbor
vote was.

Copy forward PA2/PA6. A skeleton lives at `learning/PA7/kNN_select.py`.
**Stdlib plus matplotlib only. GAI should not implement this for you.**

## 1. Hold out a test slice, then choose `k` on the rest

On `small.arff` (required) and `medium.arff` (required, use `--normalize zscore`):

1. Shuffle with a fixed seed (`--seed`, default 5) and hold out 20% of the
   rows as a **test** set. Do not use those rows to pick `k`.
2. On the remaining 80%, evaluate each `k` in `--k-grid` (default
   `1,3,5,7,9`) with leave-one-out. Record accuracy and macro-F1 for each
   `k`.
3. Choose the `k` with the best **macro-F1** on that 80% (tie-break: smaller
   `k`).
4. Refit the idea of kNN on the full 80% (every test query uses the 80% as
   its neighbor pool; this is not leave-one-out on the test rows).
5. Report accuracy, macro-F1, the confusion matrix, and per-class F1 **on
   the 20% test set only**.

Also print the majority-class baseline on the test set, using the majority
label of the 80% pool.

## 2. Soft predictions

For each test instance, store the **vote fraction** of the predicted class
(`votes_for_winner / k`). This is a crude probability.

In the report:

- Mean vote fraction on correct test predictions vs incorrect ones
- A table of test errors that includes true label, predicted label, and
  vote fraction
- A short note on whether mistakes were low-confidence

You do not need a proper scoring rule, but if you want one, Brier score on
the one-hot label vs the vote distribution is enough.

## 3. Outputs

Write `learning/PA7/output_select.md` and a plot of macro-F1 vs `k` on the
80% slice. Run:

```bash
task pa7
task pa7 DATA=learning/resources/data/medium.arff NORMALIZE=zscore
```

Closing writeup:

- Which `k` won on each file, and did test macro-F1 match the validation
  ranking?
- What happens to rare-class recall as `k` grows?
- Would you ship the `k` from validation, or do you want a nested scheme?

## Acceptance criteria

- `learning/PA7/kNN_select.py` runs via `task pa7` and honors `--k-grid`,
  `--seed`, `--normalize`, and `--distance`.
- `k` is chosen on the 80% slice; the headline metrics are from the 20%
  test slice.
- Vote fractions appear in the report.
- The markdown includes the comparison writeup.

## References

- RA8
- [Brier score](https://en.wikipedia.org/wiki/Brier_score)

# [Programming Assignment 3] A kNN Ensemble

RA2 distinguished bagging (diversity from data) from other committees. This
ticket implements bagging as the primary ensemble, then keeps a
three-distance vote as a comparison so you can see the difference.

Copy forward your latest kNN (PA6/PA2). A skeleton lives at
`learning/PA3/kNN_ensemble.py`. **Stdlib only for the model; matplotlib is
fine for optional plots. GAI should not implement this for you.**

Use leave-one-out at the **instance** level: when scoring row `i`, row `i`
is never in any member's neighbor pool. Bootstrap draws are taken from the
remaining rows.

## 1. Bagged kNN (required)

- `--members` (default 5): number of bootstrap kNNs.
- `--seed` (default 5).
- Each member draws `n-1` rows **with replacement** from the leave-one-out
  pool (same size as the pool).
- Each member uses the same `k` and the same distance (Euclidean unless
  `--distance` says otherwise) and the same `--normalize` rule as PA6.
- The ensemble prediction is majority vote over members. Break ties
  deterministically.
- Also produce a confusion matrix for each member so you can see whether
  they actually disagree.

## 2. Distance committee (comparison)

Run three kNNs on the same leave-one-out pool with Euclidean, Manhattan, and
Minkowski (`--p`). Majority-vote those three. This is the “reuse the
distances we already had” ensemble. It is not bagging.

## 3. Single kNN

Run one unbagged kNN with the same `k`, distance, and normalization so the
report has a baseline that is not the majority-class dummy (you may still
include that dummy).

## Outputs

Write `learning/PA3/output_ensemble.md` with settings, time, memory, and
confusion matrices / macro-F1 for: single kNN, bagged ensemble, each bagged
member, and the distance committee.

Run:

```bash
task pa3
task pa3 DATA=learning/resources/data/medium.arff NORMALIZE=zscore
```

Closing writeup:

- Did the members disagree, or did bagging just copy one kNN five times?
- Did bagging beat the single model on macro-F1, or only on accuracy?
- How did the distance committee compare to bagging? Which kind of
  diversity seemed to matter on these files?

## Acceptance criteria

- `learning/PA3/kNN_ensemble.py` runs via `task pa3`.
- Bagging is implemented with replacement draws and leave-one-out exclusion
  of the query.
- The markdown report includes single, bagged, and distance-committee
  results plus the writeup.

## References

- RA2
- [Bootstrap aggregating](https://en.wikipedia.org/wiki/Bootstrap_aggregating)

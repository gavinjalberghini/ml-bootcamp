# [pa-ensemble] A kNN Ensemble

You need: pa-scaled (`ScaledKNN.predict_one`, `leave_one_out`) and pa-metrics
(`metrics_report`). ra-ensembles answered.

You will: bag copies of **that** classifier, then compare a three-distance
committee. Do not reimplement distance. **GAI should not implement this
for you.**

## Steps

1. Open `learning/pa-ensemble/kNN_ensemble.py`. Keep `import_pa('pa-scaled')` and
   `import_pa('pa-metrics')`. `EnsembleKNN` subclasses `ScaledKNN`. Required
   methods have sudo comments.
2. Implement `bagged_loo(features, labels, members, seed)`:
   - For each query row `i`, the pool is every row except `i`.
   - Each member draws `len(pool)` rows **with replacement** from that pool
     (use `random.Random(seed)` plus a per-member offset).
   - Each member is a `ScaledKNN` with the same `k`, distance, and
     `--normalize`. Call `predict_one` on its bootstrap pool.
   - Ensemble vote is majority over members. Reuse `vote` from pa-knn if you
     can.
   - Also store each member's prediction so the report can show disagreement.
3. Implement `distance_committee_loo`: three `ScaledKNN` instances with
   Euclidean, Manhattan, and Minkowski (`self.p`), same `k` and normalize,
   majority vote. This is not bagging; it is the comparison ra-ensembles asked for.
4. Run a single unbagged `leave_one_out` (inherited) as the baseline.
5. Score single, bagged, and committee with `ReportingKNN.metrics_report`.
6. Write `learning/pa-ensemble/output_ensemble.md` with settings, time, memory
   (optional), confusion matrices or metric tables, and per-member macro-F1.
7. Run:

   ```bash
   task ensemble
   task ensemble DATA=learning/resources/data/medium.arff NORMALIZE=zscore
   ```

8. Answer in the markdown:
   - Did the members disagree, or did bagging copy one kNN five times?
   - Did bagging beat the single model on macro-F1, or only on accuracy?
   - How did the distance committee compare to bagging?
9. Commit and open a PR.

## Command-line contract

`data`, `--k`, `--distance`, `--p`, `--normalize`, `--members` (default 5),
`--seed` (default 5), `--output` (default `output_ensemble.md`).

## What to turn in

- `learning/pa-ensemble/kNN_ensemble.py`
- `output_ensemble.md` with the three answers

## Acceptance criteria

- Bags are drawn from the leave-one-out pool; the query row is never in a
  bag.
- Neighbor search is `ScaledKNN.predict_one`, not a new kNN.
- Report includes single, bagged, and distance-committee results.
- Stretch is optional. Skipping `stretch_feature_subspace` does not block ra-streaming.

## Stretch goal (optional)

**Challenge:** On `stretch_feature_subspace`, give each bagged member only
some of the columns. Write `learning/pa-ensemble/stretch.md`. Do not change the
required `bagged_loo` signature later tickets do not even call.

## References

- ra-ensembles
- [Bootstrap aggregating](https://en.wikipedia.org/wiki/Bootstrap_aggregating)

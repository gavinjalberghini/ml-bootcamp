# [pa-online] Online kNN for Drifting Streams

You need: pa-scaled (`predict_one`, `read_arff`, `--normalize`), pa-metrics
(`metrics_report`), ra-drift, ra-imbalance, and ra-cost. Batch leave-one-out is finished.

You will: keep that predictor and change **how instances arrive**. Memory
is a sliding window. Evaluation is prequential. **GAI should not implement
this for you.** Stdlib only for the model.

## Steps

1. Open `learning/pa-online/online_knn.py`. Keep `import_pa('pa-scaled')` and
   `import_pa('pa-metrics')`. `OnlineKNN` subclasses `ScaledKNN`. Required methods
   have sudo comments.
2. Read the `%` comments on `learning/resources/data/small_stream.arff`
   (drift index, weights, label map).
3. Implement `run_stream(features, labels)`:
   - Walk the file in order. For each new row, **predict first** using only
     the current window as `pool_x` / `pool_y` (`predict_one` from pa-scaled).
   - Then append the row and its **true** label. If the window is longer
     than `--window`, drop the oldest row.
   - You cannot store the whole stream.
   - If the window has fewer than `k` rows, skip the prediction or vote
     among what you have, and say which in the report.
   - If `--normalize` is not `none`, fit the scaler on the **current
     window** only (already the rule in `scale_pair` if the pool is the
     window).
4. Override `vote` so that `--weighted-vote` weights each neighbor by
   `1 / count(class)` in the **current window** (ra-cost). Off: same majority
   vote as pa-knn.
5. After the pass, use `ReportingKNN.metrics_report` for overall and
   per-class metrics. Also build a table of prequential accuracy and
   minority-class recall every N instances (N = 50 is fine) so the drop at
   the drift index is visible.
6. Run, in order:

   ```bash
   task online
   task online WINDOW=20
   task online:weighted
   uv run learning/pa-online/online_knn.py learning/resources/data/small.arff --k 3 --window 50
   ```

   Optional: `medium_stream.arff` (drift at 1000).
7. Write `learning/pa-online/output_online.md` with settings, time, memory,
   confusion matrix, per-class P/R/F1, the rolling table, two window sizes,
   uniform vs weighted votes, and a short comparison: stationary
   `small.arff` vs `small_stream.arff`, small `W` vs large `W`, weighted vs
   uniform.
8. Commit and open a PR.

`task generate-stream` rebuilds the stream files if you want a different
schedule. That is optional.

## Command-line contract

`data`, `--k`, `--window`, `--normalize`, `--weighted-vote`, `--output`
(default `output_online.md`).

## What to turn in

- `learning/pa-online/online_knn.py`
- `output_online.md` covering the runs in step 6

## Acceptance criteria

- Neighbor search is inherited `predict_one`. You did not paste a new kNN.
- Memory is bounded by `W`.
- The report includes window-size and weighted-vote comparisons.
- Stretch is optional. Skipping `stretch_drift_alarm` does not block lr-jetson.

## Stretch goal (optional)

**Challenge:** Mark suspected drift times on `stretch_drift_alarm` using
only the rolling accuracy table, without reading the file header. Write
`learning/pa-online/stretch.md`. Do not make `task online` call that method.

## References

- [Prequential evaluation (River)](https://riverml.xyz/latest/introduction/getting-started/prequential-evaluation/)
- [ARFF](https://waikato.github.io/weka-wiki/formats_and_processing/arff/)
- ra-drift, ra-imbalance, ra-cost

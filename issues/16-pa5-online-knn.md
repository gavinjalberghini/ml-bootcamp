# [Programming Assignment 5] Online kNN for Drifting Streams

You need: PA6 (`predict_one`, `read_arff`, `--normalize`), PA2
(`metrics_report`), RA5, RA6, and RA9. Batch leave-one-out is finished.

You will: keep that predictor and change **how instances arrive**. Memory
is a sliding window. Evaluation is prequential. **GAI should not implement
this for you.** Stdlib only for the model.

## Steps

1. Open `learning/PA5/online_knn.py`. Keep `import_pa('PA6')` and
   `import_pa('PA2')`. `OnlineKNN` subclasses `ScaledKNN`.
2. Read the `%` comments on `learning/resources/data/small_stream.arff`
   (drift index, weights, label map).
3. Implement `run_stream(features, labels)`:
   - Walk the file in order. For each new row, **predict first** using only
     the current window as `pool_x` / `pool_y` (`predict_one` from PA6).
   - Then append the row and its **true** label. If the window is longer
     than `--window`, drop the oldest row.
   - You cannot store the whole stream.
   - If the window has fewer than `k` rows, skip the prediction or vote
     among what you have, and say which in the report.
   - If `--normalize` is not `none`, fit the scaler on the **current
     window** only (already the rule in `scale_pair` if the pool is the
     window).
4. Override `vote` so that `--weighted-vote` weights each neighbor by
   `1 / count(class)` in the **current window** (RA9). Off: same majority
   vote as PA1.
5. After the pass, use `ReportingKNN.metrics_report` for overall and
   per-class metrics. Also build a table of prequential accuracy and
   minority-class recall every N instances (N = 50 is fine) so the drop at
   the drift index is visible.
6. Run, in order:

   ```bash
   task pa5
   task pa5 WINDOW=20
   task pa5:weighted
   uv run learning/PA5/online_knn.py learning/resources/data/small.arff --k 3 --window 50
   ```

   Optional: `medium_stream.arff` (drift at 1000).
7. Write `learning/PA5/output_online.md` with settings, time, memory,
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

- `learning/PA5/online_knn.py`
- `output_online.md` covering the runs in step 6

## Acceptance criteria

- Neighbor search is inherited `predict_one`. You did not paste a new kNN.
- Memory is bounded by `W`.
- The report includes window-size and weighted-vote comparisons.

## References

- [Prequential evaluation (River)](https://riverml.xyz/latest/introduction/getting-started/prequential-evaluation/)
- [ARFF](https://waikato.github.io/weka-wiki/formats_and_processing/arff/)
- RA5, RA6, RA9

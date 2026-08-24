# [pa-scaled] Scaling and Binary vs Multiclass

You need: pa-knn's `KNN` class working. ra-types and ra-scaling answered.

You will: **import** that class, not copy the file, and add scaling plus a
binary view of the same rows. Stdlib only. **GAI should not implement this
for you.**

## Steps

1. Open `learning/pa-scaled/kNN_scaled.py`. Keep the `# /// script` header and the
   `import_pa('pa-knn')` lines. `ScaledKNN` must subclass `knn.KNN`. Required
   methods have sudo comments (vague sketches, not Python).
2. If `import_pa` fails, fix pa-knn (class must be named `KNN`) rather than
   pasting pa-knn into this folder.
3. Implement `recode_labels(labels, source_path)`:
   - `--task multiclass`: return labels unchanged.
   - `--task binary` and the path contains `small`: map class `0` to `0`
     and every other class to `1` (one-vs-rest on the majority site).
   - `--task binary` and the path contains `medium` or `large`: map quality
     `<= 5` to `0` (low) and `>= 6` to `1` (high).
4. Implement `scale_pair(query, pool)`:
   - `none`: return query and pool unchanged.
   - `zscore`: mean and std **of the pool only**, per column. Zero-std
     columns become 0.
   - `minmax`: min and max of the pool only; scale to `[0, 1]`.
   Do not compute statistics on the full file.
5. Implement `predict_one` so it calls `scale_pair` and then
   `super().predict_one(...)`. `leave_one_out` should keep working from pa-knn
   because it calls `predict_one`.
6. Run, in order:

   ```bash
   task scaled
   task scaled NORMALIZE=zscore
   task scaled DATA=learning/resources/data/medium.arff NORMALIZE=none
   task scaled DATA=learning/resources/data/medium.arff NORMALIZE=zscore
   task scaled TASK=binary
   task scaled DATA=learning/resources/data/medium.arff TASK=binary NORMALIZE=zscore
   ```

7. In `learning/pa-scaled/output_scaled.md` (or a short extra section you append)
   write:
   - `small.arff` none vs z-score (multiclass): did neighbors change much?
   - `medium.arff` none vs z-score (multiclass): what changed, and which
     features were responsible?
   - Multiclass vs binary on the same file: what became easier, and what
     information did you throw away?
8. Commit and open a PR.

## Command-line contract

`data`, `--distance`, `--k`, `--p`, `--normalize {none,zscore,minmax}`,
`--task {multiclass,binary}`, `--output` (default `output_scaled.md`).

## What to turn in

- `learning/pa-scaled/kNN_scaled.py` that subclasses `knn.KNN`.
- `output_scaled.md` including the comparison writeup.

## Acceptance criteria

- pa-scaled does not contain a copied distance function; it uses `knn.KNN.dist`.
- Scaler statistics are fit without the query row.
- Binary recoding matches the rules above.
- `task scaled` runs via `uv run` on this file's script header.
- Stretch is optional. Skipping `stretch_robust_scale` does not block pa-metrics.

## Stretch goal (optional)

Later tickets only pass `--normalize {none,zscore,minmax}`. Do not replace
those names.

**Challenge:** Implement median / IQR scaling on the unused
`stretch_robust_scale` method. In `learning/pa-scaled/stretch.md`, compare it to
z-score on `medium.arff` in a one-off experiment you run by hand. Do not
make later Taskfile commands pass a new normalize value.

## References

- ra-scaling, `learning/resources/data/README.md`, `learning/load_assignment.py`

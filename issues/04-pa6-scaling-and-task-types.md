# [Programming Assignment 6] Scaling and Binary vs Multiclass

You need: PA1's `KNN` class working. RA1 and RA7 answered.

You will: **import** that class, not copy the file, and add scaling plus a
binary view of the same rows. Stdlib only. **GAI should not implement this
for you.**

## Steps

1. Open `learning/PA6/kNN_scaled.py`. Keep the `# /// script` header and the
   `import_pa('PA1')` lines. `ScaledKNN` must subclass `PA1.KNN`.
2. If `import_pa` fails, fix PA1 (class must be named `KNN`) rather than
   pasting PA1 into this folder.
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
   `super().predict_one(...)`. `leave_one_out` should keep working from PA1
   because it calls `predict_one`.
6. Run, in order:

   ```bash
   task pa6
   task pa6 NORMALIZE=zscore
   task pa6 DATA=learning/resources/data/medium.arff NORMALIZE=none
   task pa6 DATA=learning/resources/data/medium.arff NORMALIZE=zscore
   task pa6 TASK=binary
   task pa6 DATA=learning/resources/data/medium.arff TASK=binary NORMALIZE=zscore
   ```

7. In `learning/PA6/output_scaled.md` (or a short extra section you append)
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

- `learning/PA6/kNN_scaled.py` that subclasses `PA1.KNN`.
- `output_scaled.md` including the comparison writeup.

## Acceptance criteria

- PA6 does not contain a copied distance function; it uses `PA1.KNN.dist`.
- Scaler statistics are fit without the query row.
- Binary recoding matches the rules above.
- `task pa6` runs via `uv run` on this file's script header.

## References

- RA7, `learning/resources/data/README.md`, `learning/load_assignment.py`

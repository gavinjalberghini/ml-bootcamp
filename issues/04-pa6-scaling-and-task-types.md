# [Programming Assignment 6] Scaling and Binary vs Multiclass

RA1 distinguished binary and multiclass problems. RA7 explained why distance
depends on feature scale. This ticket puts both on the kNN you already wrote.

Copy forward `learning/PA1/kNN.py` into `learning/PA6/kNN_scaled.py` (a
skeleton is there). Keep leave-one-out and the three distances. Add two flags.

**Stdlib only. GAI should not implement this for you.**

## 1. `--normalize {none,zscore,minmax}`

- `none`: same behavior as PA1.
- `zscore`: subtract the mean and divide by the standard deviation, per
  feature.
- `minmax`: scale each feature to `[0, 1]`.

Fit the scaler **on the neighbor pool only**. Under leave-one-out that means:
for query `i`, compute mean/std or min/max from every row except `i`, then
apply those statistics to the query and to the pool. Do not fit on the whole
file.

If a feature has zero variance in the pool, treat its scaled value as 0.

## 2. `--task {multiclass,binary}`

- `multiclass`: use the labels as they appear in the file (PA1 behavior).
- `binary`: recode labels *before* neighbor search and scoring:
  - `small.arff`: map class `0` to `0` and every other class to `1`
    (one-vs-rest on the majority site).
  - `medium.arff` / `large.arff`: map quality `<= 5` to `0` (low) and
    quality `>= 6` to `1` (high).

The confusion matrix for `--task binary` is 2×2. You are still using the same
feature rows and the same kNN; only the label definition changed.

## 3. What to report

Write `learning/PA6/output_scaled.md` (`--output` to override) with settings,
elapsed time, and a confusion matrix. Run at least:

```bash
task pa6
task pa6 NORMALIZE=zscore
task pa6 DATA=learning/resources/data/medium.arff NORMALIZE=none
task pa6 DATA=learning/resources/data/medium.arff NORMALIZE=zscore
task pa6 TASK=binary
task pa6 DATA=learning/resources/data/medium.arff TASK=binary NORMALIZE=zscore
```

In a short section at the bottom of the markdown, compare:

- `small.arff` none vs z-score (multiclass). Did neighbors change much?
- `medium.arff` none vs z-score (multiclass). What changed, and which
  features were responsible?
- Multiclass vs binary on the same file. What became easier, and what
  information did you throw away?

## Acceptance criteria

- `learning/PA6/kNN_scaled.py` honors `--normalize` and `--task` as specified
  and runs through `task pa6`.
- Scaler statistics are fit without the query row.
- Binary recoding matches the rules above.
- `output_scaled.md` includes the comparison writeup.

## References

- RA7 and `learning/resources/data/README.md`
- [Leave-one-out and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage-during-pre-processing)

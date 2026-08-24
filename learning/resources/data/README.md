# Datasets

All files are ARFF. The last attribute is the class label. Do not include it
when you compute distance. Features are stored as `A1`, `A2`, … so parsers stay
simple; the meanings below are for you, not for the file format.

Class values are integer codes. They are categories, not quantities: quality
`6` is not “twice” class `3`, and you must not use the label in distance.

## `small.arff`

UCI Ecoli protein-localization style data. 336 instances, 7 numeric features,
8 classes. This is the default file for PA1–PA4 and PA6–PA7.

| Attribute | Meaning |
| --- | --- |
| A1 | mcg — signal sequence score (McGeoch) |
| A2 | gvh — signal sequence score (von Heijne) |
| A3 | lip — lipoprotein consensus score |
| A4 | chg — N-terminus charge on predicted lipoproteins |
| A5 | aac — amino-acid composition discriminant score |
| A6 | alm1 — membrane-spanning region score |
| A7 | alm2 — ALOM score after removing putative signal regions |
| class | localization site (see below) |

| class | Site | Count | Share |
| --- | --- | --- | --- |
| 0 | cp (cytoplasm) | 143 | 42.6% |
| 1 | im (inner membrane) | 77 | 22.9% |
| 7 | pp (periplasm) | 52 | 15.5% |
| 4 | imU (inner membrane, uncleavable) | 35 | 10.4% |
| 5 | om (outer membrane) | 20 | 6.0% |
| 6 | omL (outer membrane lipoprotein) | 5 | 1.5% |
| 2 | imS (inner membrane, signal) | 2 | 0.6% |
| 3 | imL (inner membrane, cleavable) | 2 | 0.6% |

This is already a multiclass, imbalanced problem. A classifier that always
predicts `0` is about 43% accurate and useless on the rare sites.

## `medium.arff`

UCI Wine Quality (white). 4898 instances, 11 numeric features, quality scores
treated as 7 classes. Feature ranges differ by orders of magnitude (density
near 1, residual sugar in the tens, total sulfur dioxide in the hundreds), so
unscaled distances are dominated by a few columns. That is intentional; RA7
and PA6 exist because of it.

| Attribute | Meaning |
| --- | --- |
| A1 | fixed acidity |
| A2 | volatile acidity |
| A3 | citric acid |
| A4 | residual sugar |
| A5 | chlorides |
| A6 | free sulfur dioxide |
| A7 | total sulfur dioxide |
| A8 | density |
| A9 | pH |
| A10 | sulphates |
| A11 | alcohol |
| class | quality score 3–9 |

| class | Count | Share |
| --- | --- | --- |
| 3 | 20 | 0.4% |
| 4 | 163 | 3.3% |
| 5 | 1457 | 29.7% |
| 6 | 2198 | 44.9% |
| 7 | 880 | 18.0% |
| 8 | 175 | 3.6% |
| 9 | 5 | 0.1% |

## `large.arff`

Same schema and class proportions as `medium.arff`, expanded to 19592
instances. Use it as a stress set for timing, memory, and PA4 GPU comparison.
Leave-one-out on this file is expensive; a subsample or a holdout is fine
unless a ticket says otherwise.

## Stream files

`small_stream.arff` and `medium_stream.arff` are generated from the stationary
files (`task generate-stream`). They keep the same attributes and class values,
add light jitter, inject a sudden real concept drift (label map), and change
class weights after the drift index. Read the `%` comments at the top of each
file for seed, drift index, weights, and the label map.

## Binary task (PA6)

When a ticket asks for a binary view of the same files:

- `small.arff`: keep only classes `0` and `1` (the two most frequent sites),
  or treat `0` as the positive class and every other label as `not-0`
  (one-vs-rest). The assignment says which.
- `medium.arff`: map quality `<= 5` to `low` and quality `>= 6` to `high`.

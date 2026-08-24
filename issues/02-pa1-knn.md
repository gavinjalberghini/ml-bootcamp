# [Programming Assignment 1] Implement kNN on Stationary Data

You need: RA1 done. `uv run learning/ENV/hello.py` works. You have read
`learning/resources/data/README.md`.

You will: implement a **class** `KNN` in `learning/PA1/kNN.py`. Later tickets
import that class. Do not use scikit-learn or any other ML library. Stdlib
only. **GAI should not write the implementation for you.**

The skeleton already has the class, method names, a PEP 723 header, and the
CLI. Keep those. Each required method has a **sudo** comment: a vague sketch
of the idea, not runnable Python. Rewrite it yourself.

## Steps

1. Open `learning/PA1/kNN.py`. Confirm the file starts with `# /// script`
   and `dependencies = []`. Run nothing until the methods work.
2. Implement `read_arff`. Skip `%` comments and `@` header lines. After
   `@data`, split each row on commas. The last field is the label (a
   string). The other fields are floats. Do not put the label in the
   feature vector.
3. Implement `dist` for `--distance` 1 (Euclidean), 2 (Manhattan), and 3
   (Minkowski with exponent `self.p`).
4. Implement `vote`. Majority label among the neighbor labels. Choose a
   deterministic tie-break (for example: nearest of the tied classes, then
   lowest class id). Write the rule in `output_knn.md`.
5. Implement `predict_one(query, pool_x, pool_y)`. Compute distance from
   `query` to every row in `pool_x`, take `self.k` nearest, return `vote`.
   The query must not appear in the pool.
6. Implement `leave_one_out`. For each index `i`, call `predict_one` on row
   `i` with the pool equal to every row except `i`. Return `(y_true, y_pred)`.
   Do not train on the full file and then score the same rows.
7. Implement `confusion_matrix` so rows and columns are labeled with class
   ids.
8. From the repo root run:

   ```bash
   uv run learning/PA1/kNN.py learning/resources/data/small.arff --k 3 --distance 1
   ```

   or `task pa1`. Open `learning/PA1/output_knn.md` and check the matrix
   shape matches the classes in the data README.
9. Run once on `medium.arff` (`task pa1 DATA=learning/resources/data/medium.arff K=5`)
   so you see the cost. You do not need a polished writeup for wine yet.
   Do **not** scale features in this ticket.
10. Commit the implementation and `output_knn.md` for `small.arff`. Open a PR.

## Command-line contract

Keep the flags the skeleton already parses: `data`, `--distance {1,2,3}`,
`--k`, `--p`, `--output` (default `output_knn.md`).

## What to turn in

- Working `learning/PA1/kNN.py` with class `KNN` and the methods above.
- `learning/PA1/output_knn.md` from a `small.arff` run (settings, time,
  tie-break rule, labeled confusion matrix).

## Acceptance criteria

- `task pa1` and `task pa1 DATA=learning/resources/data/medium.arff K=5` run
  under `uv run` with no project venv.
- Leave-one-out excludes the query row.
- `--distance` selects Euclidean, Manhattan, or Minkowski.
- The class is named `KNN` so PA6 can do `import_pa('PA1').KNN`.
- Stretch is optional. Skipping `stretch_cosine` does not block PA6.

## Stretch goal (optional)

Stretch goals are extra challenge. Skip this if you want. Later tickets
**never call** `stretch_cosine`. Leave it unimplemented.

**Challenge:** Implement cosine as a separate idea of “near” on that unused
method and write `learning/PA1/stretch.md`: on `small.arff`, did any
leave-one-out guesses change versus Euclidean? Do not add a fourth
`--distance` value that later CLIs do not know about.

## References

- [k-nearest neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
- [Distance metrics](https://www.kdnuggets.com/2020/11/most-popular-distance-metrics-knn.html)
- [Multiclass confusion matrix](https://www.analyticsvidhya.com/blog/2021/06/confusion-matrix-for-multi-class-classification/)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [ARFF](https://waikato.github.io/weka-wiki/formats_and_processing/arff/)

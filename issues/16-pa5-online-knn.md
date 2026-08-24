# [Programming Assignment 5] Online kNN for Drifting Streams

By this point the kNN is a batch learner: it sees a complete ARFF file, then
evaluates with leave-one-out. Real online problems do not work that way.
Instances arrive one at a time, memory must stay bounded, and both the
decision boundary and the class proportions can change while you are still
predicting.

RA5: concept drift can invalidate old neighbors. RA6: class imbalance can
make accuracy look fine while a minority label is ignored. RA9: you can
change the vote instead of pretending classes are equal. This ticket puts
those three ideas on one sliding-window kNN.

**GAI should not implement the assignment for you; feel free to use it when
you are stuck.** Stdlib only for the model. matplotlib is fine for optional
plots. A skeleton lives at `learning/PA5/online_knn.py`.

## 1. Online kNN

Process the stream instance by instance using **prequential** evaluation:
predict the label of the new instance using only the neighbors currently in
memory, then insert the instance (with its true label) into memory. Memory
must be a sliding window of the most recent `W` instances — you cannot store
the entire stream. Reuse a distance from your earlier kNN (Euclidean is the
default). Honor `--normalize` if you apply scaling: fit on the current
window only, never on the future.

The first few instances (window not yet of size `k`) cannot be predicted
fairly; skip them or predict the majority of what you have, and say which.

As you work, consider:

- Which parts of batch kNN no longer make sense once data arrives one
  instance at a time?
- What happens to predictions immediately after a sudden drift if the
  window is still full of the old concept?
- What happens to minority-class recall if the window is dominated by the
  majority class?
- How does changing `W` trade adaptation speed against stability?

## 2. `--weighted-vote` (required flag, run both ways)

When `--weighted-vote` is set, neighbors vote with weight inverse to the
class count **in the current window** (RA9). When it is off, use uniform
majority vote. Compare the two on `small_stream.arff` in the report.

## 3. The data

Start with the provided stream files. They use the same attributes and class
values as `small.arff` / `medium.arff`, but they are ordered as a stream with
a sudden concept drift and a change in class proportions. The `%` comments
at the top of each file tell you the drift index, the pre/post class
weights, and the label map.

- `learning/resources/data/small_stream.arff` — 800 instances, drift at
  instance 400. Primary dataset.
- `learning/resources/data/medium_stream.arff` — 2000 instances, drift at
  instance 1000. Optional harder run.
- `learning/resources/data/small.arff` — stationary baseline. Run the same
  online kNN over this file treated as a stream (no injected drift).

The generator is `learning/resources/generate_stream.py`
(`task generate-stream`). Reading it or changing the drift schedule is
optional.

## 4. Outputs

Write `learning/PA5/output_online.md` (`--output`) including:

- Command-line settings (`k`, `W`, distance, normalize, weighted-vote, file)
- Execution time and peak memory
- Overall prequential accuracy plus a confusion matrix
- Per-class precision, recall, and F1
- A table of prequential accuracy (and minority-class recall) every N
  instances so the drop around the drift point is visible
- The same metrics for at least two window sizes on `small_stream.arff`
- Uniform vote vs `--weighted-vote` on `small_stream.arff`
- A short written comparison: stationary `small.arff` vs `small_stream.arff`,
  small `W` vs large `W`, and weighted vs uniform votes

The script must accept the ARFF path plus at least `--k`, `--window`,
`--weighted-vote`, and `--output`.

```bash
task pa5
task pa5 WINDOW=20
# then a weighted-vote run, e.g.
# uv run learning/PA5/online_knn.py learning/resources/data/small_stream.arff --k 3 --window 50 --weighted-vote
```

Also run the same binary against `small.arff`.

## Acceptance criteria

- `learning/PA5/online_knn.py` implements prequential sliding-window kNN
  and writes `learning/PA5/output_online.md`.
- Memory is bounded by `W`.
- The report includes window-size and weighted-vote comparisons and the
  writeup above.

## References

- [Prequential evaluation (River)](https://riverml.xyz/latest/introduction/getting-started/prequential-evaluation/)
- [Concept drift](https://www.geeksforgeeks.org/machine-learning/introduction-to-concept-drift/)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [ARFF](https://waikato.github.io/weka-wiki/formats_and_processing/arff/)
- RA5, RA6, RA9

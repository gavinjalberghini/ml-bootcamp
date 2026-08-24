# [Programming Assignment 4] GPU-Assisted kNN

You need: PA6 (`ScaledKNN`) and PA2 (`metrics_report`). RA4 answered.

You will: subclass `ScaledKNN`, replace the pair loop with an array distance
matrix, and compare times. Voting and ARFF stay on the inherited class.
**GAI should not implement this for you.**

Dependencies live in **this file's** `# /// script` header. Start with
`dependencies = []` and a vectorized CPU path (stdlib lists or, if you
add it to the header, numpy). When you have CUDA, add
`"cupy-cuda12x[ctk]>=13.0"` to that list and run the same command again.
Do not use `uv sync --extra`.

## Steps

1. Open `learning/PA4/knn_gpu.py`. Keep `import_pa('PA6')` and
   `class GpuKNN(PA6.ScaledKNN)`.
2. Implement `array_module()`: return `cupy` if it imports, else a CPU
   array library or a documented fallback.
3. Implement `pairwise_distances(queries, pool, xp)` as broadcast or matrix
   math. No Python loop over every pair.
4. Override `leave_one_out` so it builds that matrix, still **excludes the
   query row** (mask or delete the diagonal), applies `--normalize` the PA6
   way (fit on the pool), and calls inherited `vote`.
5. Predictions on `small.arff` should match `ScaledKNN` except for floating
   point noise. Use `ReportingKNN.metrics_report` to compare.
6. Time CPU-loop (`task pa6`), vectorized CPU, and GPU if present, on
   `small.arff` and on `medium.arff` or a documented subsample of
   `large.arff`.
7. Write `learning/PA4/output_gpu.md` (settings, times, backend, metrics)
   and fill `learning/PA4/findings.md`: hardware, the script-header change
   you made, what moved, transfer cost, when the GPU helped, and how this
   would change for the **window** kNN in PA5.
8. Run `task pa4`. Commit and open a PR.

## Command-line contract

`data`, `--k`, `--normalize`, `--output` (default `output_gpu.md`).

## What to turn in

- `learning/PA4/knn_gpu.py`
- `output_gpu.md` and `findings.md`

## Acceptance criteria

- Distance work is array-parallel. `read_arff` and `vote` come from earlier
  classes.
- `small.arff` predictions match PA6 within floating-point noise.
- Findings say whether CuPy was in the script header and what `uv run`
  installed.

## References

- [CuPy](https://docs.cupy.dev/en/stable/)
- [uv script dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)
- [PyTorch tensors](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) (allowed alternative)
- RA4

# [Programming Assignment 4] GPU-Assisted kNN

RA4 argued that the expensive part of kNN is the distance matrix. This ticket
restructures that work so it can run on a GPU, then compares it to the CPU
kNN you already trust.

You may use CuPy, PyTorch, or another GPU array library for the distance
math. The rest of the assignment (ARFF, leave-one-out driver, voting,
metrics) stays yours. **GAI should not implement this for you.**

A skeleton lives at `learning/PA4/knn_gpu.py`. The project extra
`pa4-gpu` installs `cupy-cuda12x`. Use `task pa4` (CPU-only environment) and
`task pa4:gpu` (extra installed). If this machine has no GPU, the script
must still run: detect the missing device, compute on CPU with the same
vectorized code path if you can, and say so in the findings.

## What to implement

- Same leave-one-out protocol as PA1/PA6. Query row excluded.
- Honor `--k` and `--normalize {none,zscore,minmax}` (fit the scaler on the
  pool, not the whole file).
- Build distances as an array operation (broadcast or pairwise matrix), not
  a Python loop over every pair if you can avoid it. The GPU path and the
  CPU path should share that structure so the comparison is fair.
- Predictions should match the CPU implementation except for floating-point
  noise.
- Measure wall-clock time for CPU vs GPU (or CPU-loop vs CPU-vectorized vs
  GPU) on `small.arff` and at least one larger file (`medium.arff` or
  `large.arff`). Leave-one-out on `large.arff` is a stress run; a fixed
  subsample is acceptable if you document the size.

Write any extra setup in `learning/PA4/findings.md` as well as the comparison.

## Outputs

- `learning/PA4/knn_gpu.py` runnable via `task pa4` and `task pa4:gpu`
- `learning/PA4/output_gpu.md` with settings, times, whether a GPU was used,
  and a confusion matrix that you can set next to PA1/PA6
- `learning/PA4/findings.md`: which kernels moved, data-transfer cost, when
  the GPU helped, and how this would change if the model were the online
  window kNN from PA5 instead of batch leave-one-out

## Acceptance criteria

- Distance computation is actually array-parallel, not a thin wrapper around
  the PA1 double loop.
- CPU and GPU (or vectorized fallback) predictions are identical or
  near-identical on `small.arff`.
- Findings explain hardware, commands (`uv run --extra pa4-gpu ...`), and
  the time comparison.

## References

- [CuPy](https://docs.cupy.dev/en/stable/)
- [PyTorch tensors](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
- [Accelerated Python](https://developer.nvidia.com/blog/accelerated-python-with-cuda-and-numba/)
- RA4

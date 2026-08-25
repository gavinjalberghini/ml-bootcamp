# [ra-hardware] Heterogeneous Computing Architecture

You need: a working leave-one-out kNN. You have felt `medium.arff` get slow.

You will: identify which **method on your class** should become an array
operation in pa-gpu. You will not write GPU code in this ticket.

## Steps

1. Read [heterogeneous computing (IBM)](https://www.ibm.com/topics/heterogeneous-computing).
2. Read [what is a GPU (Intel)](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html).
3. Read [GPU computing (NVIDIA)](https://www.nvidia.com/en-us/deep-learning-ai/what-is-gpu-computing/).
4. Read [parallel computing](https://www.geeksforgeeks.org/parallel-computing/).
5. Answer every heading in `learning/ra-hardware/answers.md`:
   - What is a heterogeneous architecture?
   - CPU vs GPU design and jobs
   - Why GPUs help many ML workloads
   - Challenges of using both (memory movement, small problems)
   - Which method on `KNN` / `ScaledKNN` should move first (`dist` vs
     a new pairwise matrix)? Which methods stay on the CPU (ARFF, vote,
     the leave-one-out driver)?
   - When might GPU kNN be slower on `small.arff` than on `large.arff`?
6. Commit and open a PR.

## What to turn in

- Filled `learning/ra-hardware/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- You name the method pa-gpu will override instead of rewriting pa-knn from
  scratch.
- Stretch is optional. Skipping it does not block pa-gpu.

## Stretch goal (optional)

**Challenge:** In `learning/ra-hardware/answers.md` under “Stretch goal”, rough out
how many distance calculations leave-one-out does on `medium.arff` (rows ×
rows, plus a grain of salt). No implementation.

## Optional research

- [10.1145/3295500](https://doi.org/10.1145/3295500) via your library.

# [Reading Assignment 4] Heterogeneous Computing Architecture

Your kNN is dominated by distance calculations: every query against every
neighbor, every leave-one-out fold. That is the same arithmetic many times,
which is the kind of work GPUs are built for. CPUs and GPUs together are a
heterogeneous machine.

Read about that split, and connect it to the implementation you already have.
PA4 will ask you to restructure distance computation, not just “import cupy.”

As you read, think about the following:

- What is a heterogeneous compute architecture?
- How do CPUs and GPUs differ in design and in the jobs they are good at?
- Why are GPUs effective for many machine learning workloads?
- What challenges appear when software uses both (memory movement, branching,
  small problems that are faster on CPU)?
- Which part of *your* kNN should move to a GPU first? Which part should stay
  on the CPU (ARFF I/O, voting, the leave-one-out driver)?
- For `small.arff` vs `large.arff`, when might a GPU kNN be *slower*?

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA4/answers.md`.

## Articles

- [Heterogeneous computing (IBM)](https://www.ibm.com/topics/heterogeneous-computing)
- [What is a GPU (Intel)](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html)
- [GPU computing (NVIDIA)](https://www.nvidia.com/en-us/deep-learning-ai/what-is-gpu-computing/)
- [Parallel computing](https://www.geeksforgeeks.org/parallel-computing/)

## Research (optional)

- [10.1145/3295500](https://doi.org/10.1145/3295500) — GPU computing survey (ACM; use library access)

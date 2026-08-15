# [Programming Assignment 4] Implement GPU Assisted kNN

Description: Building on your understanding of heterogeneous compute architectures, this task focuses on adapting your existing kNN implementation to leverage GPU acceleration.

The kNN algorithm is computationally expensive due to repeated distance calculations across the dataset. GPUs can significantly improve performance by parallelising these operations. For this task, you will modify your current Python kNN implementation to utilize GPU-based computation where possible.

You may use libraries such as CuPy, PyTorch, or similar tools that provide GPU-accelerated array operations. The goal is not just to “run on GPU,” but to meaningfully restructure parts of your implementation (e.g., distance calculations) to take advantage of parallel computation.

As you work, consider the following:
- Which parts of kNN are the most computationally expensive?
- How can these operations be parallelised on a GPU?
- What changes are required to move data between CPU and GPU memory?
- What trade-offs exist between implementation complexity and performance gains?

You will compare this implementation against your CPU-based version in terms of performance and resource usage.

Acceptance Criteria:
- A GPU-accelerated version of kNN is implemented at `./learning/<your_name>/PA4/knn_gpu.py`.
- The implementation uses a GPU-enabled library (e.g., CuPy, PyTorch).
- The algorithm produces identical or near-identical predictions to the CPU version.
- Execution time is measured and compared against the CPU implementation.
- Any setup steps or dependencies are documented.
- A brief summary of findings is written in `./learning/<your_name>/PA4/findings.md`. Consult [this](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet) Markdown formatting guide as needed.

Resources:
[CuPy Documentation](https://docs.cupy.dev/en/stable/)
[PyTorch Tensor Basics](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
[GPU Acceleration in Python](https://developer.nvidia.com/blog/accelerated-python-with-cuda-and-numba/)
[kNN Optimization Strategies](https://www.geeksforgeeks.org/k-nearest-neighbors-algorithm-in-python/)

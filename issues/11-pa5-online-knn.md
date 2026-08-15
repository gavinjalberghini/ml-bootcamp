# [Programming Assignment 5] Implement Online kNN for Drifting Streams

Description: By this point the kNN is a batch learner: it sees a complete ARFF file, then evaluates with leave-one-out. Real online problems do not work that way. Instances arrive one at a time, memory must stay bounded, and both the decision boundary and the class proportions can change while you are still predicting.

You will remember from the reading assignments that concept drift can invalidate old neighbors, and that class imbalance can make accuracy look fine while a minority label is ignored. For this issue, convert kNN into an online learner and measure those effects on a stream built from the same data you have been using.

**GAI should not be used to implement the assignment for you; feel free to use it when you are stuck.**

1. Online kNN
Process the stream instance by instance using prequential evaluation: predict the label of the new instance using only the neighbors currently in memory, then insert the instance (with its true label) into memory. Memory must be a sliding window of the most recent `W` instances — you cannot store the entire stream. Reuse a distance metric from your earlier kNN (Euclidean is fine as the default). Do not use ML libraries; stdlib only.

As you work, consider the following:
- Which parts of batch kNN no longer make sense once data arrives one instance at a time?
- What happens to predictions immediately after a sudden drift if the window is still full of the old concept?
- What happens to minority-class recall if the window is dominated by the majority class?
- How does changing `W` trade adaptation speed against stability?

Prequential evaluation - https://riverml.xyz/latest/introduction/getting-started/prequential-evaluation/
Sliding window learners - https://www.geeksforgeeks.org/machine-learning/introduction-to-concept-drift/
Python command line args - https://www.tutorialspoint.com/python/python_command_line_arguments.htm

2. The Data
Start with the provided stream files. They use the same attributes and class values as `small.arff` / `medium.arff`, but they are ordered as a stream with a sudden concept drift and a change in class proportions. The `%` comments at the top of each file tell you the drift index, the pre/post class weights, and the label map.

- `./learning/resources/data/small_stream.arff` — 800 instances, drift at instance 400. Use this as your primary dataset.
- `./learning/resources/data/medium_stream.arff` — 2000 instances, drift at instance 1000. Optional harder run.
- `./learning/resources/data/small.arff` — stationary baseline. Run the same online kNN over this file treated as a stream (no injected drift) so you can compare.

The generator that built the stream files is `./learning/resources/generate_stream.py` (`task generate-stream`). You may read it, regenerate the files, or write your own generator if you want a different drift schedule. That is optional — the files above are enough to complete the assignment.

Understanding ARFF Data - https://www.cs.waikato.ac.nz/ml/weka/arff.html

3. Outputs
Write a markdown report that includes:
- Command-line settings (`k`, `W`, distance, which file)
- Execution time and peak memory
- Overall prequential accuracy plus a confusion matrix
- Per-class precision, recall, and F1 (these matter more than accuracy on the imbalanced stream)
- A table of prequential accuracy (and minority-class recall) every N instances so the drop around the drift point is visible
- The same metrics for at least two window sizes on `small_stream.arff`
- A short written comparison: stationary `small.arff` vs `small_stream.arff`, and small `W` vs large `W`

Acceptance Criteria: Create `./learning/<your_name>/PA5/online_knn.py` that runs prequential sliding-window kNN and writes the report to `./learning/<your_name>/PA5/output_online.md`. The script should accept the ARFF path plus at least `--k`, `--window`, and `--output`. Run it against `small_stream.arff` and `small.arff`.

# [Reading Assignment 3] Data Flow and Sampling Contexts

You need: batch kNN (PA1–PA3). Every evaluation so far assumed a complete
file.

You will: learn batch vs stream and sampling so the later drift tickets are
not a surprise. You will not write stream code until PA5.

## Steps

1. Read [batch vs stream processing](https://www.geeksforgeeks.org/difference-between-batch-processing-and-stream-processing/).
2. Read [streaming data (IBM)](https://www.ibm.com/topics/streaming-data).
3. Read [data sampling](https://www.geeksforgeeks.org/data-analysis/what-is-data-sampling/).
4. Read [stratified sampling](https://www.geeksforgeeks.org/stratified-sampling-in-machine-learning/).
5. Answer every heading in `learning/RA3/answers.md`:
   - When batch vs streaming
   - Challenges of streaming data
   - How poor sampling biases a model
   - How sampling changes kNN (including the leave-one-out scores you have)
   - If you subsample `medium.arff` or `large.arff`, what stratified sampling
     preserves that a file prefix would not
6. Commit and open a PR.

## What to turn in

- Filled `learning/RA3/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- You can say, in one sentence, why PA5 cannot use leave-one-out on the
  whole stream.
- Stretch is optional. Skipping it does not block RA4.

## Stretch goal (optional)

**Challenge:** In `learning/RA3/answers.md` under “Stretch goal”, design a
stratified subsample of `large.arff` (how many rows, how you keep rare
qualities). No code that later tickets import.

## Optional research

- [10.1145/2528412](https://doi.org/10.1145/2528412) via your library.

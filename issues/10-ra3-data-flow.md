# [Reading Assignment 3] Data Flow and Sampling Contexts

So far every kNN you wrote assumed a file that is complete before you start.
That is batch learning. Many real systems never have that file: instances
arrive over time, you cannot store everything, and the sample you train on
is a choice, not “all the data.”

Read about batch vs streaming (online) processing, and about sampling
(random, stratified). You will need this for the drift and imbalance readings
and for PA5.

As you read, think about the following:

- When would you prefer batch processing over streaming, and vice versa?
- What challenges arise when working with streaming data?
- How can poor sampling introduce bias into a model?
- How might sampling strategies impact kNN (including the leave-one-out
  scores you have been reporting)?
- If you subsample `medium.arff` or `large.arff` to save time, what would
  stratified sampling preserve that a naive prefix of the file would not?

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA3/answers.md`.

## Articles

- [Batch vs stream processing](https://www.geeksforgeeks.org/difference-between-batch-processing-and-stream-processing/)
- [Streaming data (IBM)](https://www.ibm.com/topics/streaming-data)
- [Data sampling](https://www.geeksforgeeks.org/data-analysis/what-is-data-sampling/)
- [Stratified sampling](https://www.geeksforgeeks.org/stratified-sampling-in-machine-learning/)

## Research (optional)

- [10.1145/2528412](https://doi.org/10.1145/2528412) — data stream processing survey (ACM; use library access)

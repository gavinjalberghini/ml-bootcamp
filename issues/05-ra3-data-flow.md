# [Reading Assignment 3] Data Flow and Sampling Contexts

Description: As we continue building toward more realistic machine learning systems, it is important to understand how data is handled in practice. For this task, you will explore the differences between batch data processing and streaming data processing, as well as common data sampling techniques.

Begin by reviewing how batch processing works, where models are trained on static datasets, and contrast this with streaming (or online) processing, where data arrives continuously and models may need to update incrementally. Consider the trade-offs between these approaches in terms of performance, scalability, and implementation complexity.

Additionally, read about data sampling methods. In real-world scenarios, it is often impractical or unnecessary to use all available data. Understanding how to properly sample data (e.g., random sampling, stratified sampling) is critical to building reliable models and evaluations.

As you read, think about the following:
- When would you prefer batch processing over streaming, and vice versa?
- What challenges arise when working with streaming data?
- How can poor sampling introduce bias into a model?
- How might sampling strategies impact the performance of kNN?

Acceptance Criteria: Read from the supporting documentation below and write your answers to the above questions in `./learning/<your_name>/RA3/answers.md`. Consult [this](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet) markdown formatting guide as needed.

Articles:
[Batch vs Streaming Data Processing](https://www.geeksforgeeks.org/difference-between-batch-processing-and-stream-processing/)
[Streaming Data in Machine Learning](https://www.ibm.com/topics/streaming-data)
[Introduction to Data Sampling](https://www.geeksforgeeks.org/data-analysis/what-is-data-sampling/)
[Stratified Sampling Explained](https://www.geeksforgeeks.org/stratified-sampling-in-machine-learning/)

Research:
https://dl.acm.org/doi/10.1145/2528412

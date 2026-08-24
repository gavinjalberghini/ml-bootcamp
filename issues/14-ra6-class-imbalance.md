# [Reading Assignment 6] Class Imbalance in Data Streams

You already met imbalance in PA2: `small.arff` is 43% class 0, and two
classes have two rows. A model can report high accuracy while almost never
recognizing the minority class. This reading steps from that static fact to
the stream setting, where the imbalance ratio is not a property of a file —
it can shift, and majority and minority roles can swap.

Read about imbalance on static datasets (oversampling, undersampling,
cost-sensitive learning, and why accuracy is a poor headline metric). Then
focus on why the stream setting is harder. Concept drift and class imbalance
often occur together, which is why per-class metrics over time matter more
than a single final accuracy.

As you review, consider how imbalance shows up in kNN. A majority class can
dominate the neighbor vote simply because it occupies more of the window,
even when a minority query is closest to a few true neighbors. RA9 will
take the cost-sensitive remedy further; here you should understand the
problem.

As you read, think about the following:

- What is class imbalance, and why can a high accuracy still mean the model
  is failing? Use `small.arff` or your PA2 report as a concrete example.
- How do oversampling, undersampling, and cost-sensitive learning differ as
  remedies, and what trade-offs does each introduce?
- Why do imbalance methods that assume a fixed class ratio become outdated
  on a data stream?
- How can concept drift and class imbalance interact (for example, the
  minority class becoming the majority after a drift)? Look at the pre- and
  post-drift weights in `small_stream.arff`.
- How might imbalance affect kNN neighbor votes, and what window or
  sampling changes could help?

You will apply this in RA9 and PA5.

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA6/answers.md`.

## Articles

- [Imbalanced classes](https://www.geeksforgeeks.org/machine-learning/how-to-handle-imbalanced-classes-in-machine-learning/)
- [Imbalanced datasets (Google ML Crash Course)](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets)
- [A gentle introduction to imbalanced classification](https://machinelearningmastery.com/what-is-imbalanced-classification/)

## Research (optional)

- [2204.03719](https://arxiv.org/abs/2204.03719) — imbalance in data streams

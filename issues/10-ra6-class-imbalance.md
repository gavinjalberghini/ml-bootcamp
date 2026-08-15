# [Reading Assignment 6] Class Imbalance in Data Streams

Description: Most introductory classifiers, including the kNN you have been building, implicitly assume that classes appear in roughly similar proportions. When that assumption fails, a model can report high accuracy while almost never recognizing the minority class. Class imbalance is therefore a problem context you must understand before trusting stream metrics.

For this task, read about class imbalance in supervised learning and how it is usually handled on static datasets (oversampling, undersampling, cost-sensitive learning, and why accuracy is a poor headline metric). Then focus on why the stream setting is harder. In an online problem the imbalance ratio is not a fixed property of a file — it can shift over time, majority and minority roles can swap, and a resampling rule that was correct at time t can be wrong at time t+Δ. Concept drift and class imbalance often occur together, which is why per-class metrics over time matter more than a single final accuracy.

As you review these materials, consider how imbalance shows up in kNN. A majority class can dominate the neighbor vote simply because it occupies more of the window, even when a minority query is closest to a few true neighbors.

As you read, think about the following:
- What is class imbalance, and why can a high accuracy still mean the model is failing?
- How do oversampling, undersampling, and cost-sensitive learning differ as remedies, and what trade-offs does each introduce?
- Why do imbalance methods that assume a fixed class ratio become outdated on a data stream?
- How can concept drift and class imbalance interact (for example, the minority class becoming the majority after a drift)?
- How might imbalance affect kNN neighbor votes, and what window or sampling changes could help?

You will apply this understanding in the programming assignment that follows. Notes may be beneficial.

Acceptance Criteria: Read from the supporting documentation below and write your answers to the above questions in `./learning/<your_name>/RA6/answers.md`. Consult [this](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet) markdown formatting guide as needed.

Articles:
- [How to Handle Imbalanced Classes in Machine Learning](https://www.geeksforgeeks.org/machine-learning/how-to-handle-imbalanced-classes-in-machine-learning/)
- [Handling Imbalanced Data for Classification](https://www.geeksforgeeks.org/machine-learning/handling-imbalanced-data-for-classification/)
- [Imbalanced Datasets (Google ML Crash Course)](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets)
- [A Gentle Introduction to Imbalanced Classification](https://machinelearningmastery.com/what-is-imbalanced-classification/)

Research:
https://arxiv.org/abs/2204.03719

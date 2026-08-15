# [Reading Assignment 5] Concept Drift in Online Learning

Description: In Reading Assignment 3 you compared batch processing with streaming data. In a real stream the difficulty is not only that instances arrive one at a time — the meaning of the data can change while the model is still learning. That change is called concept drift, and it is one of the central challenges of online / continual learning.

For this task, read about concept drift as a problem context for machine learning. You should understand the formal idea that the joint distribution P_t(x, y) can differ from P_{t+Δ}(x, y), the common temporal patterns of drift, and the difference between a change that invalidates the decision boundary (real concept drift) and a change that only shifts which regions of a still-valid boundary are observed (virtual / covariate drift).

Also read about how online models are evaluated and adapted. Batch leave-one-out or train/test splits assume a stationary dataset. Streaming evaluation is typically prequential: predict on the new instance first, then use its label to update the model. Adaptation strategies you will see include sliding windows, explicit drift detectors, and ensembles that add or drop classifiers as concepts appear and fade.

As you read, think about the following:
- What is concept drift, and how does real concept drift differ from virtual (covariate) drift?
- How do sudden, gradual, incremental, and recurring drift differ, and how would a model need to respond to each?
- Why do models trained in a single batch become unreliable under drift, and what does it mean to evaluate a model prequentially?
- How can a sliding window or an ensemble help a kNN adapt to drift? What trade-offs come with window size?
- How could you detect that a drift has occurred if you were not told the drift point in advance?

You will apply this understanding in the programming assignment that follows. Notes may be beneficial.

Acceptance Criteria: Read from the supporting documentation below and write your answers to the above questions in `./learning/<your_name>/RA5/answers.md`. Consult [this](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet) markdown formatting guide as needed.

Articles:
- [Introduction to Concept Drift](https://www.geeksforgeeks.org/machine-learning/introduction-to-concept-drift/)
- [Data Drift in Machine Learning](https://www.geeksforgeeks.org/machine-learning/data-drift-in-machine-learning/)
- [A Gentle Introduction to Concept Drift in Machine Learning](https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/)
- [Detecting & Handling Data Drift in Production](https://machinelearningmastery.com/detecting-handling-data-drift-in-production/)

Research:
https://doi.org/10.1109/TKDE.2018.2876857

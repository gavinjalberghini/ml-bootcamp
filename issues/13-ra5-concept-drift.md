# [Reading Assignment 5] Concept Drift in Online Learning

In RA3 you compared batch processing with streaming data. In a real stream
the difficulty is not only that instances arrive one at a time — the meaning
of the data can change while the model is still learning. That change is
called concept drift, and it is one of the central challenges of online
and continual learning.

Read about concept drift as a problem context. You should understand that
the joint distribution P_t(x, y) can differ from P_{t+Δ}(x, y), the common
temporal patterns of drift, and the difference between a change that
invalidates the decision boundary (real concept drift) and a change that
only shifts which regions of a still-valid boundary are observed (virtual
or covariate drift).

Also read about how online models are evaluated and adapted. Batch
leave-one-out or train/test splits assume a stationary dataset. Streaming
evaluation is typically prequential: predict on the new instance first, then
use its label to update the model. Adaptation strategies include sliding
windows, explicit drift detectors, and ensembles that add or drop
classifiers as concepts appear and fade.

As you read, think about the following:

- What is concept drift, and how does real concept drift differ from virtual
  (covariate) drift?
- How do sudden, gradual, incremental, and recurring drift differ, and how
  would a model need to respond to each?
- Why do models trained in a single batch become unreliable under drift, and
  what does it mean to evaluate a model prequentially?
- How can a sliding window or an ensemble help a kNN adapt to drift? What
  trade-offs come with window size?
- How could you detect that a drift has occurred if you were not told the
  drift point in advance?
- The stream files in `learning/resources/data/` document a sudden drift and
  a label map in their header comments. Is that real drift, virtual drift,
  or both? Why?

You will apply this in PA5.

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA5/answers.md`.

## Articles

- [Introduction to concept drift](https://www.geeksforgeeks.org/machine-learning/introduction-to-concept-drift/)
- [Data drift](https://www.geeksforgeeks.org/machine-learning/data-drift-in-machine-learning/)
- [A gentle introduction to concept drift](https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/)
- [Detecting and handling data drift](https://machinelearningmastery.com/detecting-handling-data-drift-in-production/)

## Research (optional)

- [10.1109/TKDE.2018.2876857](https://doi.org/10.1109/TKDE.2018.2876857)

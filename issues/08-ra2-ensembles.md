# [Reading Assignment 2] Ensemble Algorithms

A single classifier often misses structure that a committee can catch.
Ensemble learning combines models so the group is more stable or more
accurate than any one member.

Read about why ensembles work, and about bagging and boosting as two
different ways to create diversity. Then think about how those ideas apply
to kNN — not only “run three distances,” but whether resampling the training
rows (bagging) or reweighting mistakes (boosting) makes sense for a
memory-based model.

As you read, think about the following:

- How might you combine predictions from multiple kNN models?
- What is the difference between diversity from **data** (bootstrap samples)
  and diversity from **the distance**?
- What benefits could an ensemble provide over a single kNN?
- What challenges or trade-offs appear (cost, correlation of members,
  boosting on a model with no trainable weights)?
- Why is bagging a more natural first ensemble for kNN than boosting?

You will implement a bootstrap (bagged) kNN in PA3, and compare it to a
three-distance committee.

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA2/answers.md`.

## Articles

- [Ensemble learning (Scholarpedia)](http://www.scholarpedia.org/article/Ensemble_learning)
- [Ensemble learning (Wikipedia)](https://en.wikipedia.org/wiki/Ensemble_learning)
- [Bootstrap aggregating](https://en.wikipedia.org/wiki/Bootstrap_aggregating)
- [Boosting (Wikipedia)](https://en.wikipedia.org/wiki/Boosting_(machine_learning))
- [Bagging (IBM)](https://www.ibm.com/topics/bagging)

## Research (optional)

- Zhou, Z.-H. *Ensemble Methods: Foundations and Algorithms*. Access via
  your library; DOI overview articles include
  [10.1002/widm.1249](https://doi.org/10.1002/widm.1249).

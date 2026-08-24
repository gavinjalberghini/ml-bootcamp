# [ra-ensembles] Ensemble Algorithms

You need: a working single kNN (pa-scaled) and honest metrics (pa-metrics). You have not
combined models yet.

You will: learn bagging vs boosting so pa-ensemble can bag **your existing class**
instead of inventing a new algorithm. Boosting is reading-only; vanilla kNN
has no trainable weights to boost.

## Steps

1. Read [ensemble learning (Scholarpedia)](http://www.scholarpedia.org/article/Ensemble_learning)
   or [Wikipedia](https://en.wikipedia.org/wiki/Ensemble_learning).
2. Read [bootstrap aggregating](https://en.wikipedia.org/wiki/Bootstrap_aggregating).
3. Read [boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning)).
4. Read [bagging (IBM)](https://www.ibm.com/topics/bagging).
5. Answer every heading in `learning/ra-ensembles/answers.md`:
   - How might you combine predictions from multiple kNN models?
   - Diversity from **data** (bootstrap) vs diversity from **distance**
   - Benefits over a single kNN
   - Cost and correlation trade-offs
   - Why bagging is a more natural first ensemble for kNN than boosting
6. Commit and open a PR.

## What to turn in

- Filled `learning/ra-ensembles/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- You can describe, in one paragraph, the bagging loop pa-ensemble will run on
  `ScaledKNN`.
- Stretch is optional. Skipping it does not block pa-ensemble.

## Stretch goal (optional)

**Challenge:** In `learning/ra-ensembles/answers.md` under “Stretch goal”, explain
why stacking is a poor first extra for *this* kNN (no learned weights, LOO
cost). Do not implement stacking.

## Optional research

- [10.1002/widm.1249](https://doi.org/10.1002/widm.1249) via your library.

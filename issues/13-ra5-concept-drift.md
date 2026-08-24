# [Reading Assignment 5] Concept Drift in Online Learning

You need: RA3 (batch vs stream). Look at the `%` comments on
`learning/resources/data/small_stream.arff` before you write.

You will: learn real vs virtual drift and prequential evaluation. PA5 will
implement a sliding window on your existing `predict_one`.

## Steps

1. Open `small_stream.arff` and read the header comments (seed, drift index,
   weights, label map).
2. Read [introduction to concept drift](https://www.geeksforgeeks.org/machine-learning/introduction-to-concept-drift/).
3. Read [data drift](https://www.geeksforgeeks.org/machine-learning/data-drift-in-machine-learning/).
4. Read [a gentle introduction to concept drift](https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/).
5. Read [detecting and handling data drift](https://machinelearningmastery.com/detecting-handling-data-drift-in-production/).
6. Answer every heading in `learning/RA5/answers.md`:
   - Real vs virtual (covariate) drift
   - Sudden, gradual, incremental, recurring
   - Why batch models fail; what prequential evaluation is
   - Sliding windows vs ensembles; window-size trade-offs
   - How you would detect drift without being told the index
   - Is the provided stream drift real, virtual, or both? Why, using the
     header's label map?
7. Commit and open a PR.

## What to turn in

- Filled `learning/RA5/answers.md`.

## Acceptance criteria

- Every heading has an answer.
- You cite the stream file's drift index and label map in the last answer.

## Optional research

- [10.1109/TKDE.2018.2876857](https://doi.org/10.1109/TKDE.2018.2876857)

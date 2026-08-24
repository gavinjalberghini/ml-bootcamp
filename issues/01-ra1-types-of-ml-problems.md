# [Reading Assignment 1] Types of Machine Learning Problems

You need: ENV done (`uv run` works). You have not written a classifier yet.

You will: learn which prediction problem these files are, so PA1 is not a
guess. The datasets are classification. They are not multilabel. Class codes
are categories, not numeric targets.

## Steps

1. Read `learning/resources/data/README.md` all the way through. Note the
   class counts on `small.arff` and `medium.arff`.
2. Read [classification vs regression](https://www.geeksforgeeks.org/machine-learning/ml-classification-vs-regression/).
3. Read [classification (IBM)](https://www.ibm.com/topics/classification-machine-learning).
4. Read [types of classification tasks](https://machinelearningmastery.com/types-of-classification-in-machine-learning/).
5. Skim the [scikit-learn multiclass / multilabel notes](https://scikit-learn.org/stable/modules/multiclass.html)
   for problem types only. You will not use that library in the PAs.
6. Open `learning/RA1/answers.md`. Write an answer under each heading:
   - How does classification differ from regression?
   - What distinguishes multiclass from multilabel?
   - How do evaluation metrics change with the classification type?
   - What challenges arise as the number of classes or labels increases?
   - Which type is `small.arff`? Which type is `medium.arff`? What would you
     change to make one binary, or (hypothetically) multilabel?
7. Commit `learning/RA1/answers.md` and open a pull request.

## What to turn in

- The filled `learning/RA1/answers.md` on a PR.

## Stretch goal (optional)

Stretch goals are extra challenge. Skip this if you want. Later tickets
never read this heading.

**Challenge:** Find one real **multilabel** dataset (name it and link it).
In `learning/RA1/answers.md` under “Stretch goal”, say how a kNN would have
to change its *output* (not just its distance) to handle that file. Do not
implement it.

## Acceptance criteria

- Every required heading in the answers file has a written answer.
- You name the problem type of both provided files using the data README,
  not a guess.
- Stretch is optional. Skipping it does not block PA1.

## References

Markdown help: [cheatsheet](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet).

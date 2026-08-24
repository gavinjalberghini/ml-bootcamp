# [Reading Assignment 1] Types of Machine Learning Problems

Before you write a classifier, you need to know what kind of prediction problem
you are solving. This reading is about classification: how a model is trained
and evaluated, and how binary, multiclass, and multilabel problems differ.

The datasets in `learning/resources/data/` are classification problems. They are
not multilabel, and the class codes are not numeric targets. You will implement
only kNN in this mentorship; the point of RA1 is to know which problem kNN is
solving on these files, and which problems it is not.

As you read, think about the following:

- How does classification differ from regression?
- What distinguishes multiclass from multilabel problems?
- How do evaluation metrics change depending on the classification type?
- What challenges arise as the number of classes or labels increases?
- Which type is `small.arff`? Which type is `medium.arff`? What would you have
  to change about the files or the label to turn one of them into a binary
  problem, or (hypothetically) a multilabel problem?

You will build on this in PA1 and PA6. Notes may be beneficial.

## Acceptance criteria

Read the supporting documentation and write answers to the questions above in
`learning/RA1/answers.md`. Consult [this](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet)
markdown guide as needed. Use the dataset README at
`learning/resources/data/README.md` when you map problem types to the files.

## Articles

- [Classification vs regression (GeeksforGeeks)](https://www.geeksforgeeks.org/machine-learning/ml-classification-vs-regression/)
- [Classification in machine learning (IBM)](https://www.ibm.com/topics/classification-machine-learning)
- [Types of classification tasks (Machine Learning Mastery)](https://machinelearningmastery.com/types-of-classification-in-machine-learning/)
- [Multiclass classification (scikit-learn user guide)](https://scikit-learn.org/stable/modules/multiclass.html) — read for the problem types; do not use the library in later PAs
- [Multilabel classification (scikit-learn user guide)](https://scikit-learn.org/stable/modules/multiclass.html#multilabel-classification)

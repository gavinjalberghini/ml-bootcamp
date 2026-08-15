# [Programming Assignment 2] Visualizing Machine Learning Outputs

In this issue, I would like you to create standardised visualisations for the output of your kNN algorithm. In the future, we will gather metrics from multiple sources and at multiple time points. For this ticket, that means your kNN should provide the following:

- A confusion matrix is provided as a graphic or table.
- All metrics outlined below in a table. Be sure to calculate per-class metrics accordingly.
- The execution time of your algorithm.
- The amount of memory expended by your Python process.

ML Metrics - https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234
Classification and Regression Metrics - https://towardsdatascience.com/20-popular-machine-learning-metrics-part-1-classification-regression-evaluation-metrics-1ca3e282a2ce

Classification Accuracy = ?
Precision = ?
Recall = ?
F1-Score = ?
Sensitivity = ?
Specificity = ?

Resources
Python Mem Usage - https://www.geeksforgeeks.org/monitoring-memory-usage-of-a-running-python-program/
ML Metrics - https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234
MC Confusion Matrix - https://www.analyticsvidhya.com/blog/2021/06/confusion-matrix-for-multi-class-classification/
Matplotlib tutorials - https://matplotlib.org/stable/tutorials/introductory/sample_plots.html
Matplotlib 3D plots - https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

Acceptance Criteria: Create `./learning/<your_name>/PA2/kNN_report.py` that outputs the specified information as a file. Run it against `./learning/resources/data/small.arff` and `./learning/resources/data/medium.arff`.

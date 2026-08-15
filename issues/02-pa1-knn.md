# [Programming Assignment 1] Implement kNN Supervised Learning Algorithm in Python (Static Data)

**Description:** The kNN algorithm is a commonly used tool for performing supervised machine learning tasks. For this ticket, you will write an implementation of the kNN algorithm for the multi-class classification problem. The output of your model should be a confusion matrix as well as compiled metrics. Do not use any ML libraries. Write this implementation yourself. The use of online references is allowed and encouraged. This should be implemented in a WSL2 environment.

**GAI should not be used to implement the assignment for you; feel free to use it when you are stuck**

1. The KNN Algorithm
The kNN algorithm should read an ARFF data file from the command line. In addition to implementing the core algorithm, implement three different distance calculations (Use the kdnuggets ref for assistance picking algorithms). Toggle which distance algorithm is used via a command-line flag. The algorithm should output the elapsed time, selected distance measure, and full confusion matrix as a file.

kNN Sudo - https://towardsdatascience.com/k-nearest-neighbours-introduction-to-machine-learning-algorithms-18e7ce3d802a
Distance Measures - https://www.kdnuggets.com/2020/11/most-popular-distance-metrics-knn.html
MC Confusion Matrix - https://www.analyticsvidhya.com/blog/2021/06/confusion-matrix-for-multi-class-classification/
Python command line args tutorial - https://www.tutorialspoint.com/python/python_command_line_arguments.htm
Python 3 docs - https://docs.python.org/3/tutorial/
Python for beginners - https://www.youtube.com/watch?v=kqtD5dpn9C8
WSL2 - https://www.youtube.com/watch?v=eId6K8d0v6o&pp=ygUVc2V0dXAgd3NsMiB3aW5kb3dzIDEx

2. The Data
ARFF data is a particular data format that is common for machine learning. The header of each file specifies the layout of the data. In our case, the last value of a data point is the class value. Be sure you are not including this value when you calculate distance.

Understanding ARFF Data - https://www.cs.waikato.ac.nz/ml/weka/arff.html

**Acceptance Criteria:** The file kNN.py is created at `./learning/<your_name>/PA1/kNN.py`, and can ingest and learn on static data files (provided in `./learning/resources/data/small.arff`), then output the desired information.

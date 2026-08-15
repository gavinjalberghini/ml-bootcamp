# [Programming Assignment 3] Implement a kNN Ensemble

Description: By this point, we have refined our basic kNN algorithm. Now we can begin to make improvements based on what we are learning. To kick off this process, we will start with implementing an ensemble of kNN classifiers. You will remember in Reading Assignment 2 that there are various means of leveraging ensemble learning to improve performance.

For this issue, implement an ensemble of three kNNs. Have each kNN utilize a different distance calculation from your previous implementation. Be sure to think about how to reconcile the output of each classifier into one prediction.

Acceptance Criteria: Create a new implementation named `./learning/<your_name>/PA3/kNN_ensemble.py` that outputs the information from all classifiers as well as the final combined confusion matrix into a file named `./learning/<your_name>/PA3/output_ensemble.md`.

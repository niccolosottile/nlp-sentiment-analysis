# Implementing a Naive Bayes classifier
import numpy as np
from scipy import sparse

class ImplementedNB:
    """
    Class which implements a simplified Naive Bayes classifier:
        - It has binary class prediction (for neg or pos)
        - The prior probabilities are equal (0.5) for each class, which 
        works due to equal splitting of data (maintained by stratified sampling)
    """
    def __init__(self):
        """Initiates the simple NB classifier."""
        self.feature_log_prob = None

    def fit(self, X, y):
        """Trains the simple NB classifier using the data and labels provided."""
        # Define array to store counts for each feature (separated by class)
        feature_count = np.zeros((2, X.shape[1]))

        # Calculate counts for neg and pos reviews
        feature_count[0, :] = np.sum(X[y == 0, :], axis=0)
        feature_count[1, :] = np.sum(X[y == 1, :], axis=0)

        # Adding Laplace smoothing
        feature_count += 1

        # Calculate counts among each class
        class_count = np.sum(feature_count, axis=1)

        # Calculate the log probability of each feature given a class
        self.feature_log_prob = np.log(feature_count / class_count[:, np.newaxis])

    def predict(self, X):
        """Predicts the values for the simple NB classifier using the data provided."""
        # Ensure that X is in Compressed Sparse Row (CSR) format for efficient dot product
        if not sparse.isspmatrix_csr(X):
            X = sparse.csr_matrix(X)

        # Calculate the class probabilities for each review
        # Since we are maximising, and the prior probabilities are both 0.5, they can be ignored
        class_probabilities = X.dot(self.feature_log_prob.T)
        
        # Choose the class with higher probability for each review (indices correspond with class)
        # Dot product between CSR matrix and array results in array (np can be applied)
        predictions = np.argmax(class_probabilities, axis=1)

        return predictions
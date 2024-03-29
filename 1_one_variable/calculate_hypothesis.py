import numpy as np


def calculate_hypothesis(X, theta, i):
    """
        :param X            : 2D array of our dataset
        :param theta        : 1D array of the trainable parameters
        :param i            : scalar, index of current training sample's row
    """
    hypothesis = 0.0

    hypothesis = X[i, 0] * theta[0] + X[i, 1] * theta[1]

    return hypothesis


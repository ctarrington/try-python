import numpy as np


def evaluate_polynomial_value(x_value, weights):
    unweighted = np.array([x_value ** i for i in range(weights.shape[0])])
    return np.dot(unweighted, weights)


def build_a(order, xs):
    return np.array([[x ** p for p in range(order + 1)] for x in xs])

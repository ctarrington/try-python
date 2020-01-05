import math
import numpy as np
import matplotlib.pyplot as plt


def evaluate_polynomial_value(x_value, weights):
    unweighted = np.array([x_value ** i for i in range(weights.shape[0])])
    return np.dot(unweighted, weights)


def build_a(order, xs):
    return np.array([[x ** p for p in range(order + 1)] for x in xs])


def calculate_rms_error(xs, ys, weights):
    predicted_y = [ evaluate_polynomial_value(x, weights) for x in xs]
    errors = np.square(predicted_y - ys)
    return math.sqrt(np.sum(errors)/xs.shape[0])


def plot_points_over_fit(point_label, point_color, domain, xs, ys, weights, order):
    predicted_x = np.linspace(domain[0], domain[1], 100)
    predicted_y = [ evaluate_polynomial_value(x, weights) for x in predicted_x]
    plt.plot(predicted_x, predicted_y, color='grey', label='fit line')
    plt.plot(xs, ys, marker='o', linestyle='None', color=point_color, label=point_label)
    plt.ylim(-1.3, 1.3)

    rms_error = calculate_rms_error(xs, ys, weights)

    title = 'n: ' + str(xs.shape[0]) + ' Order: ' + str(order) + ' RMS error: ' + str(rms_error)
    plt.legend()
    plt.title(title)
    plt.show()
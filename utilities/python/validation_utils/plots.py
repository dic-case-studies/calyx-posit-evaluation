import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt

import math
import numpy as np
import json

import scipy as sp
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error

print("Setting matplot configurations")
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
# matplotlib.rcParams['text.usetex'] = True


def decimal_accuracy(expected, actual):
    if expected == 0:
        if actual == 0:
            return math.inf
        else:
            return 0
    if (actual/expected) <= 0:
        return 0
    v = abs(math.log10(actual/expected))
    if v == 0:
        return math.inf
    return -math.log10(v)


def relative_error(expected, actual):
    return 100.0 * ((expected - actual) / expected)


def plot_accuracy_error(path, v, expected, actual, dpi=300):
    fig, ax = plt.subplots(1,2, figsize = (10,5))

    accuracy = []
    error = []
    for i, (e, a) in enumerate(zip(expected, actual)):
        accuracy.append(decimal_accuracy(e, a))
        calc_error = relative_error(e, a)
        error.append(calc_error)

    ax[0].set_title(f"Decimal Accuracy-{v} \n(Higher is better)")
    ax[0].plot(accuracy)
    ax[0].set_ylim(0, 10)
    ax[0].set_xlabel("Idx")
    ax[0].set_ylabel("Accurate Digits")
    
    ax[1].set_title(f"Relative Error-{v} \n(Lower is better)")
    ax[1].set_xlabel("Idx")
    ax[1].set_ylabel("%")
    ax[1].plot(error)
    ax[1].set_ylim(0, 1.5)

    fig.tight_layout()
    fig.savefig(path, dpi=dpi)

    # expected_np, actual_np = np.array(expected), np.array(actual)
    # mse_none = mean_squared_error(expected_np, actual_np)
    # ssim_none = ssim(expected_np, actual_np, data_range=actual_np.max() - actual_np.min())

    # print("------------------------------------")
    # print(f"                {v}                ")
    # print("------------------------------------")
    # print("Mean Square Error: ", mse_none)
    # print("Structural Similarity: ", ssim_none)
    # print("------------------------------------")

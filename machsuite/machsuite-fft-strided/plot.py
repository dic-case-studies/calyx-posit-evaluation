import json
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import math

# matplotlib.rcParams['pdf.fonttype'] = 42
# matplotlib.rcParams['ps.fonttype'] = 42
# matplotlib.rcParams['text.usetex'] = True

cpp_reference = {}

with open("cpp_actual.json") as raw:
    cpp_reference = json.load(raw)

posit_actual = {}

with open("output_double.json") as raw:
    posit_actual = json.load(raw)

def decimal_accuracy(expected, actual):
    v = abs(math.log10(actual/expected))
    if v == 0:
        return math.inf
    return -math.log10(v)

def relative_error(expected, actual):
    return 100.0 * ((expected - actual) / expected)

from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error

var = ['rel', 'img']

fig, ax = plt.subplots(2, 2)
idx = 0

for v in var:
    expected = cpp_reference[v]
    actual = posit_actual['memories'][v]

    expected_np, actual_np = np.array(expected), np.array(actual)
    mse_none = mean_squared_error(expected_np, actual_np)
    ssim_none = ssim(expected_np, actual_np, data_range=actual_np.max() - actual_np.min())

    print("------------------------------------")
    print(f"                {v}                ")
    print("------------------------------------")
    print("Mean Square Error: ", mse_none)
    print("Structural Similarity: ", ssim_none)
    print("------------------------------------")

    accuracy = []
    error = []
    for i, (e, a) in enumerate(zip(expected, actual)):
        accuracy.append(decimal_accuracy(e, a))
        calc_error = relative_error(e, a)
        error.append(calc_error)
        
        if (calc_error > 1):
            print(i)
            print(e, a)

    ax[idx, 0].set_title(f"Decimal Accuracy-{v} \n(Higher is better)")
    ax[idx, 0].plot(accuracy)
    ax[idx, 0].set_ylim(0, 10)
    ax[idx, 0].set_xlabel("Idx")
    ax[idx, 0].set_ylabel("Accurate Digits")
    
    ax[idx, 1].set_title(f"Relative Error-{v} \n(Lower is better)")
    ax[idx, 1].set_xlabel("Idx")
    ax[idx, 1].set_ylabel("%")
    ax[idx, 1].plot(error)
    ax[idx, 1].set_ylim(0, 1.5)

    idx = idx + 1

plt.tight_layout()
plt.savefig("plot.png")

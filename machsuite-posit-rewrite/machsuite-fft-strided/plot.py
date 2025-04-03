import json
from validation_utils.plots import plot_accuracy_error

vars = [
    {"name": 'real', "var_name": 'rel'},
    {"name": 'imag', "var_name": "img"}
]

with open("fft.out.double.json") as f:
    data_actual = json.load(f)

with open("fft.expect.double.json") as f:
    data_expect = json.load(f)

for v in vars:
    plot_accuracy_error(
        f'machsuite-fft-strided-{v["name"]}.png',
        v["name"],
        data_actual['memories'][v["var_name"]],
        data_expect[v["var_name"]]['data']
    )

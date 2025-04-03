import json
from validation_utils.plots import plot_accuracy_error

vars = [
    {"name": 'out', "var_name": 'out'}
]

with open("spmv.out.double.json") as f:
    data_actual = json.load(f)

with open("spmv.expect.double.json") as f:
    data_expect = json.load(f)

for v in vars:
    plot_accuracy_error(
        'machsuite-spmv-crs.png',
        v["name"],
        data_actual['memories'][v["var_name"]],
        data_expect[v["var_name"]]['data']
    )

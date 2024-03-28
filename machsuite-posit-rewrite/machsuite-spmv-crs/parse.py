import json

# Rather ugly parsing code

var_names = ["val", "cols", "row_delimiters", "vec", "out"]
in_data = {}
out_data = {}

with open("input.data", "r+") as f:
    idx = 0
    arr = []
    for line_raw in f:
        line = line_raw.strip()
        if line != "%%":
            # print(line)
            arr.append(float(line))
        else:
            if idx != 0:
                in_data[var_names[idx-1]] = {
                "data": arr,
                "format": {
                    "numeric_type": "bitnum",
                    "is_signed": False,
                    "width": 32
                    }
                }
                arr = []
            idx += 1
    in_data["vec"] = {
                "data": arr,
                "format": {
                    "numeric_type": "bitnum",
                    "is_signed": False,
                    "width": 32
                    }
                }


out_data_val = {}
with open("check.data", "r+") as f:    
    idx = 0
    arr = []
    for line_raw in f:
        line = line_raw.strip()
        if line != "%%":
            arr.append(float(line))

    out_data_val = {
                "data": arr,
                "format": {
                    "numeric_type": "bitnum",
                    "is_signed": False,
                    "width": 32
                    }
                }
out_data = in_data.copy()
out_data["out"] = out_data_val
in_data["out"] = out_data_val


############ Write float test data

with open("spmv.in.double.json", "w+") as f:
    f.write(json.dumps(in_data))

with open("spmv.expect.double.json", "w+") as f:
    f.write(json.dumps(out_data))

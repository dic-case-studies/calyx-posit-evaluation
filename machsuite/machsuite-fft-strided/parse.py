import json

# Rather ugly parsing code

var_names = ["rel", "img", "rel_twid", "img_twid"]
in_data = {}
out_data = {}

with open("input.data", "r+") as f:
    idx = 0
    arr = []
    for line_raw in f:
        line = line_raw.strip()
        if line != "%%":
            print(line)
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
    in_data["img_twid"] = {
                "data": arr,
                "format": {
                    "numeric_type": "bitnum",
                    "is_signed": False,
                    "width": 32
                    }
                }


with open("check.data", "r+") as f:    
    idx = 0
    arr = []
    for line_raw in f:
        line = line_raw.strip()
        if line != "%%":
            arr.append(float(line))
        else:
            if idx != 0:
                out_data[var_names[idx-1]] = {
                "data": arr,
                "format": {
                    "numeric_type": "bitnum",
                    "is_signed": False,
                    "width": 32
                    }
                }
                arr = []
            idx += 1
    out_data["img"] = {
                "data": arr,
                "format": {
                    "numeric_type": "bitnum",
                    "is_signed": False,
                    "width": 32
                    }
                }

out_data["rel_twid"] = in_data["rel_twid"]
out_data["img_twid"] = in_data["img_twid"]


############ Write float test data

with open("fft.fuse.double.json", "w+") as f:
    f.write(json.dumps(in_data))

with open("fft.expect.double.json", "w+") as f:
    f.write(json.dumps(out_data))

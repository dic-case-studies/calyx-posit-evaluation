const { transform_machsuite_data_to_json } = require("../../utilities/js/machsuite-data");

const vals = [
    { field: "val", width: 32, dim: [1666], input: true, output: false },
    { field: "cols", width: 32, dim: [1666], input: true, output: false },
    { field: "row_delimiters", width: 32, dim: [495], input: true, output: false },
    { field: "vec", width: 32, dim: [494], input: true, output: false },
    { field: "out", width: 32, dim: [394], input: false, output: true }
];

transform_machsuite_data_to_json("spmv", vals);

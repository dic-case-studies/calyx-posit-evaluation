const { transform_machsuite_data_to_json } = require("../../utilities/js/machsuite-data");

const vals = [
    { field: "nzval", width: 32, dim: [494, 10], input: true, output: false },
    { field: "cols", width: 32, dim: [494, 10], input: true, output: false },
    { field: "vec", width: 32, dim: [494], input: true, output: false },
    { field: "out", width: 32, dim: [494], input: false, output: true }
];

transform_machsuite_data_to_json("spmv", vals);

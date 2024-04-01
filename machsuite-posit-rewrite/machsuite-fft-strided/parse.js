const { transform_machsuite_data_to_json } = require("../../utilities/js/machsuite-data");

const vals = [
    { field: "rel", width: 32, dim: [1024], input: true, output: true },
    { field: "img", width: 32, dim: [1024], input: true, output: true },
    { field: "rel_twid", width: 32, dim: [512], input: true, output: false },
    { field: "img_twid", width: 32, dim: [512], input: true, output: false }
];

transform_machsuite_data_to_json("fft", vals);

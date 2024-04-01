# Utility to convert machsuite data to json

## Usage

```js
const { transform_machsuite_data_to_json } = require("../../utilities/js/machsuite-data");

const vals = [
    { field: "obs", width: 8, dim: [140], input: true, output: false },
    { field: "init", width: 32, dim: [64], input: true, output: false },
    { field: "transition", width: 32, dim: [64, 64], input: true, output: false },
    { field: "emission", width: 32, dim: [64, 64], input: true, output: false },
    { field: "path", width: 32, dim: [512], input: false, output: true }
];

transform_machsuite_data_to_json("viterbi", vals);
```

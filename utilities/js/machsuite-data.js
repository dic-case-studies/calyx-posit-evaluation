const fs = require('fs');
const { assert } = require("console");

const parse_machsuite_datafile = (filename) => fs.readFileSync(filename, 'utf-8')
    .split("%%")
    .slice(1)
    .map(a => a.split("\n"))
    .map(arr => arr.filter(a => a).map(a => parseFloat(a)));

const group_2d_array = (array, nr_cols) => {
    const twoDArray = [];
    let row = 0;

    for (let idx = 0; idx < array.length; idx += nr_cols) {
        twoDArray.push([]);
        for (let col = 0; col < nr_cols; col++) {
            twoDArray[row].push(array[row * nr_cols + col]);
        }
        row++;
    }
    return twoDArray.map(a => a.filter(b => b !== undefined));
}

const dat_to_json = (data, width) => ({
    "data": data,
    "format": {
        "numeric_type": "bitnum",
        "is_signed": false,
        "width": width
    }
})

/*
    Reads input.data and check.data and create 
    <bench>.in.double.json and <bench>.expect.double.json
*/
const transform_machsuite_data_to_json = (benchmark, vals) => {
    const input_data = parse_machsuite_datafile("input.data");
    const expect_data = parse_machsuite_datafile("check.data")

    let input_json = {};
    let output_json = {};

    // Populate values for <bench>.input.double.json
    vals.filter(({ input }) => input)
        .forEach(({ field, width, dim }, idx) => {
            assert(dim.length <= 2, "Field should be a 1D or 2D array");
            const data = input_data[idx];
            const formatted_data = dim.length == 1 ? data : group_2d_array(data, dim[1]);
            input_json[field] = dat_to_json(formatted_data, width);
        });

    vals.filter(({ input, output }) => output && !input)
        .forEach(({ field, width, dim }) => {
            assert(dim.length <= 2, "Field should be a 1D or 2D array");
            let size = dim.reduce((acc, cur) => acc * cur, 1);
            const data = Array(size).fill(0);
            const formatted_data = dim.length == 1 ? data : group_2d_array(data, dim[1]);
            input_json[field] = dat_to_json(formatted_data, width);
        });

    // Populate values for <bench>.expect.double.json
    vals.filter(({ output }) => output)
        .forEach(({ field, width, dim }, idx) => {
            assert(dim.length <= 2, "Field should be a 1D or 2D array");
            const data = expect_data[idx];
            const formatted_data = dim.length == 1 ? data : group_2d_array(data, dim[1]);
            output_json[field] = dat_to_json(formatted_data, width);
        });

    fs.writeFileSync(
        `./${benchmark}.in.double.json`,
        JSON.stringify(input_json),
        'utf8'
    );
    fs.writeFileSync(
        `./${benchmark}.expect.double.json`,
        JSON.stringify({ "out": output_json }),
        'utf8'
    );
};


module.exports = {
    transform_machsuite_data_to_json
};

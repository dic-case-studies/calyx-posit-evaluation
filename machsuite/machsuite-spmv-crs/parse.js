const fs = require("fs")

const input = fs.readFileSync('./input.data', 'utf8').split("%%").slice(1).map(a => a.split("\n")).map(a => {
  const data = a.filter(a => a)
  return data.map(a => parseFloat(a))
})

const check_data = fs.readFileSync("./check.data", 'utf8').split("\n").slice(1, 495).map(a => parseFloat(a))

const format = {
    "numeric_type": "bitnum",
    "is_signed": false,
    "width": 32
  }
  
const val = { "data": input[0], format };
const cols = { "data": input[1], format };
const row_delimiters = { "data": input[2], format };
const vec = { "data": input[3], format };
const out = { "data": Array.from(check_data).fill(0), format };

const outdata = { val, cols, row_delimiters, vec, out };
fs.writeFileSync('./spmv.in.double.json', JSON.stringify(outdata), 'utf8');
fs.writeFileSync('./spmv.expect.double.json', JSON.stringify({ "out": {"data": check_data, format} }), 'utf8');

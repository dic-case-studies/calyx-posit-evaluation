const fs = require("fs")

const input = fs.readFileSync('./input.data', 'utf8').split("%%").slice(1).map(a => a.split("\n")).map(a => {
  const data = a.filter(a => a)
  return data.map(a => parseFloat(a))
})

const check_data = fs.readFileSync("./check.data", 'utf8').split("\n").slice(1, 495).map(a => parseFloat(a))

const toTwoDArrays = (array, secDim) => {
  const twoDArray = [];
  let count = 0;

  for (let i = 0; i < array.length; i += secDim) {
    twoDArray.push([]);
    for (let index = 0; index < secDim; index++) {
      twoDArray[count].push(array[count * secDim + index])
    }
    count++
  }
  return twoDArray.map(a => a.filter(b => b !== undefined));
};

const format = {
  "numeric_type": "bitnum",
  "is_signed": false,
  "width": 32
}

const nzval = { "data": toTwoDArrays(input[0], 10), format };
const cols = { "data": toTwoDArrays(input[1], 10), format };
const vec = { "data": input[2], format };
const out = { "data": Array.from(check_data).fill(0), format };

const outdata = { nzval, cols, vec, out };
fs.writeFileSync('./input.double.fuse.data', JSON.stringify(outdata), 'utf8');
fs.writeFileSync('./expected.fuse.data', JSON.stringify({ "out": check_data }), 'utf8');
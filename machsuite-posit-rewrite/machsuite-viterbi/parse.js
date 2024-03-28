const fs = require("fs")

const input = fs.readFileSync('./input.data', 'utf8').split("%%").slice(1).map(a => a.split("\n")).map(a => {
  const data = a.filter(a => a)
  return data.map(a => parseFloat(a))
})

const check_data = fs.readFileSync("./check.data", 'utf8').split("\n").slice(1, 141).map(a => parseFloat(a))
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

const obs = { "data": input[0], format };
const init = { "data": input[1], format };
const transition = { "data": toTwoDArrays(input[2], 64), format };
const emission = { "data": toTwoDArrays(input[3], 64), format };
const path = { "data": Array.from(check_data).fill(0), format };

const outdata = { obs, init, transition, emission, path };
fs.writeFileSync('./viterbi.in.double.json', JSON.stringify(outdata), 'utf8');
fs.writeFileSync('./viterbi.expect.double.json', JSON.stringify({ "path": check_data }), 'utf8');
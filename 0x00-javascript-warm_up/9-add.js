#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const input1 = parseInt(process.argv[2]);
const input2 = parseInt(process.argv[3]);
if (isNaN(input1) || isNaN(input2)) {
  console.log('NaN');
} else {
  console.log(add(input1, input2));
}

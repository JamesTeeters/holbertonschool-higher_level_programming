#!/usr/bin/node
const input = parseInt(process.argv[2]);
let x;
if (isNaN(input)) {
  console.log('Missing size');
} else {
  for (x = 0; x < input; x++) {
    console.log('X'.repeat(input));
  }
}

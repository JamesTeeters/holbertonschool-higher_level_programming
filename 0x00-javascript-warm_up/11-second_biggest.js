#!/usr/bin/node
function sub (a, b) {
  return a - b;
}
if (process.argv.length <= 3) {
  console.log('0');
} else {
  console.log(process.argv.sort(sub)[process.argv.length - 2]);
}

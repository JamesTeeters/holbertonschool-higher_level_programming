#!/usr/bin/node
const NumOfArgs = process.argv.length;
if (NumOfArgs <= 2) {
  console.log('No argument');
} else if (NumOfArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

#!/usr/bin/node
const fs = require('fs');
const fPath = process.argv[2];
fs.readFile(fPath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

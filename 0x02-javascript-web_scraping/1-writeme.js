#!/usr/bin/node
const fs = require('fs');
const cString = process.argv[3];
const fPath = process.argv[2];
fs.writeFile(fPath, cString, err => {
  if (err) {
    console.error(err);
  }
});

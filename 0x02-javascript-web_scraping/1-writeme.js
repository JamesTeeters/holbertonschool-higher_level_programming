#!/usr/bin/node
const fs = require('fs');
const cString = process.argv[3];
fs.writeFile(process.argv[2], cString, err => {
  if (err) {
    console.error(err);
  }
});

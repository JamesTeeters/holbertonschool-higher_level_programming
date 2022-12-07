#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const output = JSON.parse(body).results;
    let apperance = 0;
    for (const key in output) {
      const characters = output[key].characters;
      for (const character in characters) {
        if (characters[character].includes('/18/')) {
          apperance += 1;
        }
      }
    }
    console.log(apperance);
  }
});

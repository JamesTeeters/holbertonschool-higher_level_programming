#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const output = JSON.parse(body);
    console.log(output.title);
  }
});

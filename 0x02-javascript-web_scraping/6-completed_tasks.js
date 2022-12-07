#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const completeTask = {};
    const content = JSON.parse(body);
    for (let i = 0; i < content.length; i++) {
      const id = content[i].userId;
      const complete = content[i].completed;
      if (complete) {
        if (!completeTask[id]) {
          completeTask[content[i].userId] = 1;
        } else {
          completeTask[content[i].userId] += 1;
        }
      }
    }
    console.log(completeTask);
  }
});

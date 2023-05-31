#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const completed = {};
  body.forEach((task) => {
    if (task.completed) {
      if (!completed[task.userId]) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId] += 1;
      }
    }
  });
  console.log(completed);
});

#!/usr/bin/node

const request = require('request');
const address = process.argv[2];

request(address, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = {};

    for (const todos of JSON.parse(body)) {
      if (todos.completed) {
        if (results[todos.userId] === undefined) {
          results[todos.userId] = 0;
        }
        results[todos.userId] += 1;
      }
    }
    console.log(results);
  }
});

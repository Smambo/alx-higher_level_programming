#!/usr/bin/node

const request = require('request');
const address = process.argv[2];

request(address, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;

    for (const i in results) {
      for (const charac of results[i].characters) {
        if (charac.search('/18/') > 0) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});

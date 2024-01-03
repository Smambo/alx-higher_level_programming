#!/usr/bin/node

const request = require('request');
const address = process.argv[2];

request(address, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});

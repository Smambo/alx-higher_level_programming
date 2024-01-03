#!/usr/bin/node

//Script prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const num = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + num, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});

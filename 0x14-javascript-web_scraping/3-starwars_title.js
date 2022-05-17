#!/usr/bin/node

const request = require('request');
const episode = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const dict = JSON.parse(body);
    console.log(dict.title);
  }
});

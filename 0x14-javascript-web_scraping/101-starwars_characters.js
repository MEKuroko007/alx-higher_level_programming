#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(API_URL, function (err, res, body) {
  if (!err) {
    const chars = JSON.parse(body).chars;
    printCharacters(chars, 0);
  }
});

function printCharacters (chars, index) {
  request(chars[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        printCharacters(chars, index + 1);
      }
    }
  });
}

#!/usr/bin/node

const request = require('request');
const EPISODE_NUM = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + EPISODE_NUM, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});

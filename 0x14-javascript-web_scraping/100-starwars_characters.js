#!/usr/bin/node

const req = require('request');
const EPISODE_NUM = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
req.get(API_URL + EPISODE_NUM, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const content = data.characters;
  for (const i of content) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const dataJSON = JSON.parse(body1);
      console.log(dataJSON.name);
    });
  }
});

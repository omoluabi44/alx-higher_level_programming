#!/usr/bin/node

const res = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
res({ url, json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(body.title);
});

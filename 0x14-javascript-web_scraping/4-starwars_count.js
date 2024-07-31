#!/usr/bin/node
const res = require('request');
const url = process.argv[2];
const id = 'https://swapi-api.alx-tools.com/api/people/18/';
let total = 0;
res({ url, json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  for (let i = 0; i < body.results.length; i++) {
    for (let j = 0; j < body.results[i].characters.length; j++) {
      if (id === body.results[i].characters[j]) {
        total++;
      }
    }
  }
  console.log(total);
});

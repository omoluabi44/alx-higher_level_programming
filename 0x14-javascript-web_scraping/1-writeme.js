#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const str = process.argv[3];

fs.writeFile(filepath, str, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});

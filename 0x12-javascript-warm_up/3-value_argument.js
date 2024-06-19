#!/usr/bin/node

const argLine = process.argv.slice(2);

if (!argLine[0]) {
  console.log('No argument');
} else {
  console.log(argLine[0]);
}

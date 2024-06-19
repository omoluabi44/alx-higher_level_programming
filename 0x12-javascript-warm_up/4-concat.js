#!/usr/bin/node

const argLine = process.argv.slice(2);

if (argLine) {
  console.log(argLine[0] + ' is ' + argLine[1]);
}

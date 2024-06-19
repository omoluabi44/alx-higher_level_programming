#!/usr/bin/node

const argLine = process.argv.slice(2);

if (argLine) {
  const intFromStr = parseInt(argLine[0]);
  if (isNaN(intFromStr)) {
    console.log('Not a Number');
  } else {
    console.log(intFromStr);
  }
}

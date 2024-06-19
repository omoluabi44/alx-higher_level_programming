#!/usr/bin/node
/*
const argLine = Math.floor(Number(process.argv[2]));
console.log(isNaN(argLine) ? 'Not a Number' : `My number: ${num}`);
*/
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);

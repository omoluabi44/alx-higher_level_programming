#!/usr/bin/node

const argLine = process.argv.slice(2);

if (argLine.length === 0){
    console.log('No argument');
} else if (argLine.length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}

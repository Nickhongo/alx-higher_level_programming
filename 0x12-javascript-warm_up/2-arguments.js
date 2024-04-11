#!/usr/bin/node
const numOfArgs = process.argv.length;

if (numOfArgs === 2) {
	console.log('No argument');
} else if (numOfArgs === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

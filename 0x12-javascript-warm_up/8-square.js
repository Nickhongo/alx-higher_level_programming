#!/usr/bin/node
const loop = parseInt(process.argv[2]);
if (loop) {
	for (let j = 0; j < loop; j++) {
	console.log('X'.repeat(loop));
	}
} else {
	console.log('Missing size');
}

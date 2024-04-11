#!/usr/bin/node
let numberOfArgsPrinted = 0;

exports.logMe = function(item) {
	console.log(`${numberOfArgsPrinted}: ${item}`);
	numberOfArgsPrinted++;
};

#!/usr/bin/node
const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

fs.readFile(sourceFilePath1, 'utf8', (err1, data1) => {
	if (err1) {
		return console.error('Error reading file:', err1);
	}
	fs.readFile(sourceFilePath2, 'utf8', (err2, data2) => {
		if (err2) {
			return console.error('Error reading file:', err2);
		}
		const concatenatedData = data1 + data2;
		fs.writeFile(destinationFilePath, concatenatedData, 'utf8', (err3) => {
			if (err3) {
				return console.error('Error writing file:', err3);
			}
			console.log('Files concatenated successfully!');
		});
	});
});

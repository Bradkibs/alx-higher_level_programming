#!/usr/bin/node

const fs = require('fs').promises;
const process = require('process');
const filePath = process.argv[2];
async function read(file) {
	try {
		const data = await fs.readFile(file, 'utf-8');
		console.log(data.toString());
	}
	catch (error) {
	console.log(error);
}
}
read(filePath);

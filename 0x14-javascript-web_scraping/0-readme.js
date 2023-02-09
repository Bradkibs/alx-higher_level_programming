#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

/*
const fs = require('fs').promises;
const filePath = process.argv[2];
async function read (file) {
  try {
    const data = await fs.readFile(file, 'utf-8');
    console.log(data.toString());
  } catch (error) {
    console.log(error);
  }
}
read(filePath);
*/

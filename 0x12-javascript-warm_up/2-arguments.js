#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;
console.log(len === 2 ? 'No argument' : len === 3 ? 'Argument found' : 'Arguments found');

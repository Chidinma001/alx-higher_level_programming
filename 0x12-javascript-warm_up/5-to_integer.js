#!/usr/bin/node
const toNum = Number(process.argv[2]);
const toInt = Math.floor(toNum);
console.log(isNaN(toInt) ? "Not a number" : `My number: ${toInt}`);

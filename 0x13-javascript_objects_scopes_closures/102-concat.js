#!/usr/bin/node

const fs = require('fs');

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destPath = process.argv[4];

const file1Cont = fs.readFileSync(file1Path);
const file2Cont = fs.readFileSync(file2Path);

const concatCont = Buffer.concat([file1Cont, file2Cont]);

fs.writeFileSync(destPath, concatCont);

#!/usr/bin/node
const oldDict = require('./101-data').dict;
const newDict = {};
for (const key in oldDict) {
  if (newDict[oldDict[key]] === undefined) {
    newDict[oldDict[key]] = [key];
  } else {
    newDict[oldDict[key]].push(key);
  }
}
console.log(newDict);

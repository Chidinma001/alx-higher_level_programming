#!/usr/bin/node
const args = process.argv;
const firstArg = args[2];
const answer = typeof firstArg === "undefined" ? "No argument" : firstArg;
console.log(answer);

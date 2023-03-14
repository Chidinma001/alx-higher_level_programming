#!/usr/bin/node
let argCount = process.argv.length;
const answer = argCount === 2 ? "No argument": argCount === 3 ? "Argument found" : "Arguments found";
console.log(answer); 

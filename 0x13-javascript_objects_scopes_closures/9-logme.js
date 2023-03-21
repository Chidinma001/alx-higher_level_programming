#!/usr/bin/node
let n;
n = 0;
exports.logMe = function (item) { console.log(`${n++}: ${item}`); };

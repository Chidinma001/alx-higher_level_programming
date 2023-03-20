#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const targs = args.map(Number).slice(2, args.length).sort((a, b) => b - a);
  console.log(targs[1]);
}

#!/usr/bin/node

const args = process.argv.slice(2).map(x => Number(x));

if (args.length === undefined || args.length <= 2) {
  console.log(0);
} else {
  console.log(args.sort().reverse()[1]);
}

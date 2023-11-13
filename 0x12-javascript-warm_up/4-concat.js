#!/usr/bin/node

const arg = process.argv.slice(2);
if (arg[0] === undefined && arg[1] === undefined) {
  console.log('undefined is undefined');
} else if (arg[1] === undefined) {
  console.log(arg[0] + ' is' + ' undefined');
} else {
  console.log(arg[0] + ' is ' + arg[1]);
}

#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(Number(arg))) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < Number(arg); i++) {
    console.log('C is fun');
  }
}

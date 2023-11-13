#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(Number(arg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(arg); i++) {
    console.log('X'.repeat(arg));
  }
}

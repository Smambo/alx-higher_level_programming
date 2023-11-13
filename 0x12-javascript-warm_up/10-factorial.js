#!/usr/bin/node

const num = isNaN(Number(process.argv[2])) ? 1 : Number(process.argv[2]);

function factorialise (n) {
  if (n === 0) {
    return (1);
  } else {
    return (n * factorialise(n - 1));
  }
}
console.log(factorialise(num));

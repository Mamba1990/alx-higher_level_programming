#!/usr/bin/node
function factorial (m) {
  if (m < 0) {
    return (-1);
  }
  if (m === 0 || isNaN(m)) {
    return (1);
  }
  return (m * factorial(m - 1));
}

console.log(factorial(Number(process.argv[2])));

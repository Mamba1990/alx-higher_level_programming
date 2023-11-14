#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      let sq = '';
      for (let k = 0; k < this.width; k++) {
        sq += c;
      }
      console.log(sq);
    }
  }
}

module.exports = Square;

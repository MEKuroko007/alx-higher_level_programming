#!/usr/bin/node
const FiveSquare = require('./5-square');

class Square extends FiveSquare {
  charPrint (char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += char;
      }
      console.log(s);
    }
  }
}

module.exports = Square;

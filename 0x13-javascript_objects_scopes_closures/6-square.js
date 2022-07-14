#!/usr/bin/node
// class  that defines a square and inherits from Rectangle of 4-rectangle.js
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    let prit;

    if (c) {
      prit = ('' + c.repeat(this.width) + '\n').repeat(this.height - 1);
      prit += ('' + c.repeat(this.width));
    } else {
      prit = ('X'.repeat(this.width) + '\n').repeat(this.height - 1);
      prit += ('X'.repeat(this.width));
    }
    console.log(prit);
  }
};

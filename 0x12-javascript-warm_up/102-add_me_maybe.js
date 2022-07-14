#!/usr/bin/node
// fun that increments and calls a function.
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};

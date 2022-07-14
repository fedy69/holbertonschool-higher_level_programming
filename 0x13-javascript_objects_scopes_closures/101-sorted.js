#!/usr/bin/node
// script  that imports a dictionary of occurrences by user id and computes a dictionary of user id's by occurrence

const { dict } = require('./101-data');

const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);

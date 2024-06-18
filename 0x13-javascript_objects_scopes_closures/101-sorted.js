#!/usr/bin/node
const dict = require('./101-data').dict;
let newDict = {};
let i;
for (i in dict) {
  newDict[dict[i]] = [];
}
for (i in dict) {
  newDict[dict[i]].push(i);
}
function stay (a, b) {
  return a - b;
}
for (i in newDict) {
  newDict[i].sort(stay);
}
console.log(newDict);

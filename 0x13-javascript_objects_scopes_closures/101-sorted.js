#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const val = Object.values(dict);
const valsUniq = [...new Set(val)];
const newDict = {};
for (const k in valsUniq) {
  const list = [];
  for (const j in totalist) {
    if (totalist[j][1] === valsUniq[k]) {
      list.unshift(totalist[j][0]);
    }
  }
  newDict[valsUniq[k]] = list;
}
console.log(newDict);

#!/usr/bin/node
const fs = require('fs');
const cont = process.argv[3];

fs.writeFile(process.argv[2], cont, function (err) {
  if (err) {
    console.log(err);
  }
});

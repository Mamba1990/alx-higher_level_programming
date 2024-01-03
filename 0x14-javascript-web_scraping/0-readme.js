#!/usr/bin/node
const fs = require('fs');

<<<<<<< HEAD
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
=======
fs.readFile(process.argv[2], 'utf8', function (err, dt) {
  if (err) {
    console.log(err);
  } else {
    console.log(dt);
>>>>>>> 039aea538b610d4216b0c72f444c17e9950922a5
  }
});

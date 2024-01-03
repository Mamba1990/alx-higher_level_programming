#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request
  .get(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const dt = JSON.parse(body);
      console.log(dt.title);
    }
  });

#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (let j = 0; j < characters.length; j++) {
      request(characters[j], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});

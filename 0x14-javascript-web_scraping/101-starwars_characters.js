#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, async (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const chars = JSON.parse(body).chars;
  for (const characterUrl of chars) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});

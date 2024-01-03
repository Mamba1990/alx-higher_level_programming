#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const result = {};
    for (let j = 0; j < data.length; j++) {
      if (data[j].completed === true) {
        const todo = data[j];
        if (result[todo.userId] === undefined) {
          result[todo.userId] = 0;
        }
        result[todo.userId]++;
      }
    }
    console.log(result);
  }
});

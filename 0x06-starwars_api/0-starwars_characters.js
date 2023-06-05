#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const name = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error)
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(name);
    }
  }
});

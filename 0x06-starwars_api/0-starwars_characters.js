#!/usr/bin/node

const request = require('request');
const id = process.argv[1];
const url = https://swapi-api.alx-tools.com/api/films/{id}/;

request(url, (error, response) => {
  if(error) {
    console.log(error);
  }
  result = JSON.parse(response);
  result.characters.map((character) => {
    console.log(character.name);
  });
});

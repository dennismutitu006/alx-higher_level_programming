#!/usr/bin/node

const request = require('request');
const API_URL = process.argv[2];

request(API_URL, (err, res, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    const chars = data.results[i].characters;
    for (let j = 0; j < chars.length; j++) {
      if (chars[j].includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});

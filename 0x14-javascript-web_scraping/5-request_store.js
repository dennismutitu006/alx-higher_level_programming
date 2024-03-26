#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const path = process.argv[3];

request(URL, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(path, 'utf-8', function (err, body) {
    if (err) console.log(err);
  });
});

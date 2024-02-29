#!/bin/bash
#take a url and display of all HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

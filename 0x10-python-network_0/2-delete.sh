#!/bin/bash
#this will send a delete request to $1 URL and then display the response body
curl -s "$1" -X DELETE

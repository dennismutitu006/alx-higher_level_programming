#!/bin/bash
#It will send GET request to URL and dislpay the response body
curl -sfL "$1" -X GET

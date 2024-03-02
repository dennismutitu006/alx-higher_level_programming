#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL and
displays the value of request-Id variable found in the header of
the response.
"""
import sys
import urllib.request

# Get the url from the 1st argument
url = sys.argv[1]

# After getting the url , send a req to url and open resonse.
with urllib.request.urlopen(url) as response:
    # in the opened url get the x-requested-id var from the header
    x_req_id = response.getheader("X-Request-Id")
    print(x_req_id)
if __name__ == "__main__":

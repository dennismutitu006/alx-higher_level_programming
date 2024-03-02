#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL and
displays the value of request-Id variable found in the header of
the response.
"""
import sys
import urllib.request

# Get the url from the 1st argument
if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
# After getting the url , send a req to url and open resonse
    with urllib.request.urlopen(req) as response:
        x_req_id = response.getheader("X-Request-Id")
        print(x_req_id)

#!/usr/bin/python3
"""
The script will fetch a given URL.
"""
import urllib.request
# Script will fetch a given url with specified data
url = 'https://alx-intranet.hbtn.io/status'

# with statement to open the URL as a response object
with urllib.request.urlopen(url) as response:
    # the response body to be read in bytes
    body = response.read()
    print("Body response:")
    # print type of object
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))

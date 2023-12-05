#!/usr/bin/python3
"""funtcion returns an object"""
import json

def from_json_string(my_str):
    """will return an object"""
    return json.loads(my_str)

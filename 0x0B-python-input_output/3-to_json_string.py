#!/usr/bin/python3
"""a function tha  prints a string rep of an object"""
import json

def to_json_string(my_obj):
	""" we will use the dumps function"""
	return json.dumps(my_obj)

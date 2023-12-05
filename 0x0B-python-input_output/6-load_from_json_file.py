#!/usr/bin/python3
"""function that creates an object from a JSON file"""
import json

def load_from_json_file(filename):
	"""this fucntion will create an object using the filenme"""
	with open(filename) as k:
		return json.load(k)

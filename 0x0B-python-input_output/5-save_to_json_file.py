#!/usr/bin/python3
"""function writes an object to a textfile"""
import json

def save_to_json_file(my_obj, filename):
	"""the with statemnt will open the file for writing"""
	with open(filename, "w") as l:
		json.dump(my_obj, l)

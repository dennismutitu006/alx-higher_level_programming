#!/usr/bin/python3
"""this function will return a list of available attributes & method"""
def lookup(obj):
	"""the list to be returned"""
	return (dir(obj))

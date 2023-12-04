#!/usr/bin/python3
"""this function will return a list of available attributes & method"""


def lookup(obj):
	"""Return the list of objects available attributes and methods"""
	return (dir(obj))

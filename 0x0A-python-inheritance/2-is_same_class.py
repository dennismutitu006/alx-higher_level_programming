#!/usr/bin/python3
"""Define a class-checking function"""

def is_same_class(obj, a_class):
	"""it will check if object is an instance of a calss,
	Return true if obj is an instnace of the 
	class, otherwise return false"""
	return (type(obj) == a_class)

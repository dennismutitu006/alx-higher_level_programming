#!/usr/bin/python3
""" initialization of the defination"""
def is_kind_of_class(obj, a_class):
	"""Return True if the object is an instnace of,
	or if the object is an instnace of a class"""
	if isinstance(obj, a_class):
		return True
	return False

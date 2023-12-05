#!/usr/bin/python3
""" definaation of a function that reads a text file"""


def read_file(filename=""):
	""" read file will allow input of the file name"""
	with open(filename, encoding="utf-8") as k:
		""" do the actual readding"""
		print(f.read(), end="")

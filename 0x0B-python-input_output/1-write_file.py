#!/usr/bin/python3
"""defination of the write file function"""

def write_file(filename="", text=""):
	"""this function will have the following arguments:
	Args:
		filename: the name of the file.
		text: the text to be added.
	Return: 
		the number of character written.
	"""
	with open(filename, "w", encoding="utf-8") as l:
		return l.write(text)

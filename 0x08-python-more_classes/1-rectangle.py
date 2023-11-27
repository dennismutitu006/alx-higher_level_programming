#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
	"""this represents initialisation of a rectangle"""
	def __init__(self, width=0, height=0):
		"""Initializing the rectangle class above
		Args:
			width: represents the width of the rectangle
			height: reps the height of the rectangle
		Raise:
			TypeError: displayed if the size is not an int
			ValueError: if size is < 0
		"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""it retrieves width attribute"""
		return self.__width
	@width.setter
	def width(self, value):
		"""Sets the width attribute"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value
	@property
	def height(self):
		"""Retrieves height attribute"""
		return self.__height
	@height.setter
	def height(self, value):
		"""Sets height attribute"""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

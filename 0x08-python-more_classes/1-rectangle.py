#!/usr/bin/python3

""" A rectangle class"""


class Rectangle:
    """ Defines the properties of a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """A getter for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter for the width property"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A getter for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter for the height property"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

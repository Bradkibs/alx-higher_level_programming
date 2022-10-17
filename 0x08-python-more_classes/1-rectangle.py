#!/usr/bin/python3

class Rectangle:
    """ Defines the properties of a rectangle"""

    def __init__(self, width=0, height=0):
        """ Initializing the class """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A getter for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter for the width property"""
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A getter for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter for the height property"""
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

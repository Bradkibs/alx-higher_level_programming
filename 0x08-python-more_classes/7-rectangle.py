#!/usr/bin/python3

""" A rectangle class"""


class Rectangle:
    """ Defines the properties of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width and self.__height:
            return 2*(self.__width + self.__height)
        return 0

    def __str__(self):
        """A representation of the rectangle in pictorial format using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print(self.print_symbol, end='')
            if i is not (self.__height - 1):
                print("")
        return ""

    def __repr__(self):
        """ A representaion of the rectangle object """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ A destructor class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

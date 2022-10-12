#!/usr/bin/python3

"""A square type definition"""


class Square:
    """A class square with private instance of size and enforced size type"""

    def __init__(self, size=0):
        """An initialization function checking the type of size"""

        self.size = size

    @property
    def size(self):
        """A getter function for the size private instance attribute size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """A setter function for the value of size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """It calculates the area of the square"""

        return (self.__size ** 2)

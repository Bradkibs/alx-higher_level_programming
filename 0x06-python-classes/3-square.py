#!/usr/bin/python3

"""A square type definition"""


class Square:
    """A class square with private instance of size and enforced size type"""

    def __init__(self, size=0):
        """An initialization function checking the type of size"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """It calculates the area of the square"""

        return (self.__size ** 2)

#!/usr/bin/python3

""" A function to add two integers """



def add_integer(a, b=98):
    """Adds two numbers namely a and b if given.
    If b is not given a default value of 98 is assigned to it
    Returns the addition of two numbers as an integer"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

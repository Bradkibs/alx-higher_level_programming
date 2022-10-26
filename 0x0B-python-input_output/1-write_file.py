#!/usr/bin/python3

"""A function that writes a string to a text file"""


def write_file(filename="", text=""):
    """should write a string to a file and
    return the number of characters written"""

    with open(filename, "w+", encoding="utf-8") as filename:
        buff = filename.write(text)
    return buff

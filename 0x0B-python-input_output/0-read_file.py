#!/usr/bin/python3

"""Reads utf-8 files and prints to the stdout"""


def read_file(filename=""):
    """Reads utf-8 files"""

    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end= "")


#!/usr/bin/python3

"""A function that returns an object represented by JSON"""


import json


def from_json_string(my_str):
    """Returns a python object
    Args:
        my_str - A JSON object
        """
    return json.loads(my_str)

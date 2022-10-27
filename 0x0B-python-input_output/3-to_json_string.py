#!/usr/bin/python3
import json
"""Converting string to json"""


def to_json_string(my_obj):
    """A function that returns json representation of an object"""
    obj_to_json = json.dumps(my_obj)
    return obj_to_json

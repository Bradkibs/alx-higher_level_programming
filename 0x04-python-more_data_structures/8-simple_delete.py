#!/usr/bin/python3

#deletes a key value pair in a dictionary

def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key)
    return (a_dictionary)

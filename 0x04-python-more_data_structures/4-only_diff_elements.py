#!/usr/bin/python3

# returns a set of all elements present in only oe set

def only_diff_elements(set_1, set_2):
    diff = set_1.symmetric_difference(set_2)
    return (diff)

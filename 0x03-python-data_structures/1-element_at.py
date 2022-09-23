#!/usr/bin/python3
"""Retrieving elements using their index number"""

def element_at(my_list, idx):
    if (idx < 0):
        return None
    list_len = len(my_list)
    if (idx > list_len - 1):
        return None
    return my_list[idx]

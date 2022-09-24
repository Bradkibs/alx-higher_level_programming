#!/usr/bin/python3

"""replacing an element in a list at a specific position without modifying the original list"""


def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > (len(my_list) - 1)):
        return my_list
    new_list = [item for item in my_list]
    new_list[idx] = element
    return new_list

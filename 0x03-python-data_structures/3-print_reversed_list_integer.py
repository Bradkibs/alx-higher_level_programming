#!/usr/bin/python3

# Printing integers in a list in reverse order

def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for item in rev_list[::-1]:
        print("{:d}".format(item))

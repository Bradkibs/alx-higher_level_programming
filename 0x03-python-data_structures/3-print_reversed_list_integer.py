#!/usr/bin/python3

# Printing integers in a list in reverse order

def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    rev_list = [my_list[-i] for i in range(1, len(my_list) + 1)]
    for item in rev_list:
        print("{:d}".format(item))

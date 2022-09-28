#!/usr/bin/python3

# printing a sorted dictionary

def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")

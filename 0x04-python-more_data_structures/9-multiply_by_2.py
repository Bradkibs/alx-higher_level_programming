#!/usr/bin/python3

# returns a new dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    new_dict = {key: value for key, value in a_dictionary.items()}
    for i in new_dict:
        new_dict[i] *= 2
    return (new_dict)

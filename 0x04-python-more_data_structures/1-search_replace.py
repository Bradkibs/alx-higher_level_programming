#!/usr/bin/python3

# replaces all occurences of an element by another in a new list

def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        if i == search:
            i == replace
        new.append(i)
    return new

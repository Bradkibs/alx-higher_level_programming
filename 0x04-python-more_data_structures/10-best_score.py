#!/usr/bin/python3

# returns the key with the biggest integer

def best_score(a_dictionary):
    maximum = -1
    if not a_dictionary:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > maximum:
            maximum = a_dictionary[i]
    for b in a_dictionary:
        if a_dictionary[b] == maximum:
            return b

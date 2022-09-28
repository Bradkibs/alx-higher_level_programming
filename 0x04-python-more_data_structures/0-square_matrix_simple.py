#!/usr/bin/python3

# a function that computes the square of all matrix integers

def square_matrix_simple(matrix=[]):
    res = []
    for item in matrix:
        res.append(list(map(lambda x: x**2, item)))
    return(res)

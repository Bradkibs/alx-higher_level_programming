#!/usr/bin/python3

# printing matrix of integers

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for i in item:
            if i == item[-1]:
                print("{:d}".format(i), end="")
                break
            print("{:d} ".format(i), end="")
        print()

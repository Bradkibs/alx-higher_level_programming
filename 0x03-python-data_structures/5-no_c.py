#!/usr/bin/python3

# removes all characters of c and C from a string

def no_c(my_string):
    new =[]
    for item in range(len(my_string)):
        if my_string[item] != 'c' and my_string[item] != 'C':
            new += my_string[item]
        new_str = [i.join('') for i in new]
        print(new_str)

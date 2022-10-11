#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for item in range(x):
            my_list[x]
            i += 1
            print(my_list[item], end="")
        print()
    except IndexError:
        i = 0
        for item in my_list:
            i += 1
            print(item, end="")
        print()
    except:
        print("Unknown Error")
    return (i)


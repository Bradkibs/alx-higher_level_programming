#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        
    except ValueError as VE:
        print("Exception: {}".format(VE),file=sys.stderr)
        return (False)

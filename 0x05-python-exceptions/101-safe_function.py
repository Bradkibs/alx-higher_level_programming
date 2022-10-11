#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as excep:
        print("Exception: {}".format(excep), file=sys.stderr)
        return (None)

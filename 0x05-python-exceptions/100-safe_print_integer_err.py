#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as inst:
        print("Exception: {}".format(inst.args[0]), file=sys.stderr)
        return False

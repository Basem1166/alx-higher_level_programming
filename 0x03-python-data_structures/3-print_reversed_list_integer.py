#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_new = reversed(my_list)
    
    for x in my_list_new:
        print("{:d}".format(x))

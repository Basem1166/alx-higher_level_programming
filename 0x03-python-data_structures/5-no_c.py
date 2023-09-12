#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for letter in my_string:
        if letter is not 'c' and letter is not 'C':
            new_string += letter
    return new_string

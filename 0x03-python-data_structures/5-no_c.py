#!/usr/bin/python3


def no_c(my_string):
    new_str = ""
    for ch in my_string:
        if ord(ch) == 99 or ord(ch) == 67:
            del ch
        else:
            new_str += ch
    return new_str

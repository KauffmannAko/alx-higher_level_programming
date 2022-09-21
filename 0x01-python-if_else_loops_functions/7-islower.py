#!/usr/bin/python3
def islower(c):
    num = list(range(97, 123))
    if ord(c) in num:
        return True
    elif ord(c) not in num:
        return False

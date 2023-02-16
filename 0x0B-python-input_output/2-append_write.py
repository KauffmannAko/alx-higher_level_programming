#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Thur 16:13 2022
@author: Nana Kauffmann
"""


def append_write(filename="", text=""):
    """_appends a string to a file_

    Args:
        filename (str, optional): file path.
        text (str, optional): the string.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    f.closed
    with open(filename, encoding="utf-8") as r:
        rdfile = r.read()
    r.closed
    return len(rdfile)

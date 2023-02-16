#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Thur 16:13 2022
@author: Nana Kauffmann
"""

def read_file(filename=""):
    """Reads a file

    Args:
        filename (str, optional): the file path to open. Defaults to "".
    """
    with open(filename,encoding="utf-8") as f:
        read = f.read()

    f.closed
    print(read)
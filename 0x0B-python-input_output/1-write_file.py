#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Thur 16:13 2022
@author: Nana Kauffmann
"""
def write_file(filename="", text=""):
    """_write string to a file

    Args:
        filename (str): _file path_.
        text (str): _text to be writted_.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        writing = f.write(text)
    f.closed
    with open(filename,encoding='utf-8') as rf:
        List_of_str =rf.read()
    rf.closed
    return len(List_of_str)

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Thur 16:13 2022
@author: Nana Kauffmann
"""


import json


def save_to_json_file(my_obj, filename):
    """_Writes an object to a text file_

    Args:
        my_obj (_type_): _the object_
        filename (_type_): _file path_
    """
    obj = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(obj)
    f.closed

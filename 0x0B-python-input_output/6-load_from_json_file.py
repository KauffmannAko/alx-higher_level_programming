#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Thur 16:13 2022
@author: Nana Kauffmann
"""


import json


def load_from_json_file(filename):
    """_create an object from a json file_

    Args:
        filename (_json_): file path
    """

    with open(filename, encoding="utf-8") as f:
        fromfile = f.read()

    f.closed
    return json.loads(fromfile)

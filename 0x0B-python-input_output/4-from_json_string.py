#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Thur 16:13 2022
@author: Nana Kauffmann
"""


import json


def from_json_string(my_str):
    """_summary_

    Args:
        my_str (_type_): _description_

    Returns:
        _type_: _description_
    """

    return json.loads(my_str)
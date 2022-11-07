#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Oct. 31,2022
@author: Nana Kauffmann
"""


def inherits_from(obj, a_class):
    """
    check if a_class is a a sub class and
    obj is an instance of a_class and return
    true else false
    """
    if issubclass(type(obj), a_class) and isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Oct. 31,2022
@author: Nana Kauffmann
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of class, or if the object is an instance\
        of a class that inherited from
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on Wed Feb 17 :40:34 2022
@author: Nana Kauffmann
"""

def add_integer(a, b=98):
    """
    add two integers

     Args:
         a (int): First to add
         b (int): Second integer to add
    Raises:
          TypeError:Exception if a or b not an int or float

    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Oct. 31,2022
@author: Nana Kauffmann
"""


class BaseGeometry:
    """
    A public instance method that raises an exception
    """
    def area(self):
        raise Exception("area() is not implemented")

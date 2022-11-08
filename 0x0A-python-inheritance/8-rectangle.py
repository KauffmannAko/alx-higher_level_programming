#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Oct. 31,2022
@author: Nana Kauffmann
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
         A Rectangle class shape, inheirts from BaseGeometry
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

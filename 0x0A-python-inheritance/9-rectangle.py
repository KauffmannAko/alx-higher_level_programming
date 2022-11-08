#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Oct. 31,2022
@author: Nana Kauffmann
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A public instance method that raises an exception
    """
    def __init__(self, width, height):
        """
         A Rectangle class shape, inheirts from BaseGeometry
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        str funtion for rectangle
        Returns:
            Return width/height
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        return self.__width * self.__height

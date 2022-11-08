#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Oct. 31,2022
@author: Nana Kauffmann
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    A public instance method that raises an exception
    """
    def __init__(self, size):
        """
         A Rectangle class shape, inherits from BaseGeometry
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str funtion for rectangle
        Returns:
            Return width/height
        """
        return '[Rectangle] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        return self.__size * self.__size

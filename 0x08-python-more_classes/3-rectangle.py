#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur. Oct. 21 2022
@author: Nana Kauffmann
"""


class Rectangle:
    """Empty rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        my_str = ""
        if self.height == 0 or self.width == 0:
            return my_str
        else:
            for row in range(self.height):
                for col in range(self.width):
                    my_str += "#"
                if row < self.__height - 1:
                    my_str += '\n'
        return my_str

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

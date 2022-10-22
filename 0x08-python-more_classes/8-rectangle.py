#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur. Oct. 21 2022
@author: Nana Kauffmann
"""


class Rectangle:
    """Empty rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        my_str = ""
        if self.height == 0 or self.width == 0:
            return my_str
        else:
            for row in range(self.height):
                for col in range(self.width):
                    my_str += str(self.print_symbol)
                if row < self.__height - 1:
                    my_str += '\n'
        return my_str

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

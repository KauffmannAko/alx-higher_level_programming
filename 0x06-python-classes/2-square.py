#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur Oct 13 19:22:54 2022
@author: Nana Kaufmann
"""


class Square:
    """Square is a an empty class

    Attributes:
        size (int): The size of the square
    """
    def __init__(self, size=0):
        """The __init__ method for Square class

        Args:
            size: (:obj:'int'): A private instance size
        """
        self.__size = size
    @size.setter
    def size(self,value):
        if isinstance(value, int):
            self.__size = value
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
                                 


        


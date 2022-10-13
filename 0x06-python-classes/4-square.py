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
        Raises:
              TypeError: Exception if type is not an integer
              ValueError:Exception if is negative
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        """retrieve the size
        Returns:
           The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
          value: (:obj:'int'): new size to be set
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            self.__size = value

    def area(self):
        """Method to find area
        Returns:
              The area of the square
        """
        return self.__size * self.__size

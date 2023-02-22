#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Feb 20 22:22:09 2022
@author: nana Kauffmann
"""
from models.base import Base


class Rectangle(Base):
    """subclass
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (int, optional): _des
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width
        """
        self.__width = value

    @property
    def height(self):
        """height

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height

        Args:
            value (_type_): _description_
        """
        self.__height = value

    @property
    def x(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x

    @x.setter
    def x(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.__x = value

    @property
    def y(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x

    @y.setter
    def y(self, value):
        """s

        Args:
            value (_type_): _description_
        """
        self.__y = value

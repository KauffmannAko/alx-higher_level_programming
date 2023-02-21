#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Feb 20 22:22:09 2022
@author: nana Kauffmann
"""
from base import Base


class Rectange(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

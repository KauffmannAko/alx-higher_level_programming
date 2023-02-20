#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Feb 20 22:22:09 2022
@author: meco
"""


class Base(object):
    """ Class Base

    Attributes:
        __nb_objects (int): An integer of input id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor

        Args:
            id (int): An integer of of input id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

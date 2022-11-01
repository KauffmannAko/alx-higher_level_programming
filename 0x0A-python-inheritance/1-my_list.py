#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon. Oct. 31,2022
@author: Nana Kauffmann
"""


class MyList(list):
    """Inherit from list
    """
    def print_sorted(self):
        """
          Public instance method that print sorted list
        """
        lstCpy = self[:]
        lstCpy.sort()
        print(lstCpy)

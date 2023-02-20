#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:09 2020
@author: Nana
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit test for the Base class

    """

    def setUp(self):
        """Test Data
        """

        self.base1 = Base(5)
        self.base2 = Base(12)
        self.base3 = Base()
        self.base4 = Base()

    def test_id(self):
        """Test whether id passed is outputted
        """

        self.assertEqual(self.base1.id, 5)
        self.assertEqual(self.base2.id, 12)

    def test_increment(self):
        """Test that id is incremennted
        """

        self.assertEqual(self.base3.id, 3)
        self.assertEqual(self.base4.id, 4)


if __name__ == '__main__':
    unittest.main()

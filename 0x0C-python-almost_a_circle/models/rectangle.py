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

        # validating width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        # validating height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        # validating x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        # validating y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def update(self, *args):
        """Update arguments

        Returns:
            _type_: _description_
        """
        new_arg = []
        for i in range(len(args)):
            if args[i] is None:
                new_arg.append(args[i])
            else:
                if i == 0:
                    self.id = args[i]
                    new_arg.append(self.id)
                elif i == 1:
                    self.__width = args[i]
                    new_arg.append(self.__width)
                elif i == 2:
                    self.__height = args[i]
                    new_arg.append(self.__height)
                elif i == 3:
                    self.__x = args[i]
                    new_arg.append(self.__x)
                elif i == 4:
                    self.__y = args[i]
                    new_arg.append(self.__y)
        return tuple(new_arg)

    def area(self):
        """Area

        Returns:
            int: returns the area of a rectangle
        """
        return self.__height * self.__width

    def display(self):
        """print # char of a rectangle
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print("", end="")
            for j in range(self.__width):
                print("#", end="")
            print(" ")

    def __str__(self):
        """str method for class Rectangle
        using you don't use str magic method,you
        will have this <__main__.Demo object at 0x7f705a1addf0>
        as your output - we override the __str__ method

        Returns:
            strls: he string: [class_name] (id) x/y - width/height
        """
        string = "[{}] ({}) {}/{}".format(self.__class__.__name__, self.id,
                                          self.__x, self.__y,
                                          self.__width, self.__height)
        return string

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")
        else:
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

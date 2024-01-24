#!/usr/bin/python3
"""Module contains a class that defines a square"""


class Square:

    """defines a square"""

    def __init__(self, size=0):
        """initializes instance attributes for instances of a square

        Args:
            size: length of the square
        """
        self.size = size

    @property
    def size(self):
        """defines size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """defines lenght of a square
        Args:
            value: values representing sizes of the square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    """defines area of a square"""

    def area(self):
        return self.__size ** 2

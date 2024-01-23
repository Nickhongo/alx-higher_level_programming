#!/usr/bin/python3
"""Module contains a class that defines a square"""

class Square:
    """defines a square"""

    def __init__(self, size=0):
        """initializes instance attributes for instances of a square

        Args:
            size: length of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    """defines area of a square"""

    def area(self):
        return self.__size ** 2

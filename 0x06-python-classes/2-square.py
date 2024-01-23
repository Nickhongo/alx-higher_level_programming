#!/usr/bin/python3

"""Defines a square"""

class Square:
    """reps a square"""

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
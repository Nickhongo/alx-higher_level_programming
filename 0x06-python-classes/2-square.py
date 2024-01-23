#!/usr/bin/python3

"""Defines a class Square"""

class Square:
    """reps a square"""

    def __init__(self, size=0):
        """initialize a new square

        Args:
            size (int): length of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

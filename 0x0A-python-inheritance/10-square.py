#!/usr/bin/python3

"""
BaseGeometry: empty class
"""


class BaseGeometry:

    """
    BaseGeometry defined
    """
    def area(self):

        """Raises an exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):

    """
    classs rep a rectangle
    """

    def __init__(self, width, height):
        """
        initialises a rectangle instance
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Area of a rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):

    """
    class representing a square
    """

    def __init__(self, size):
        """
        initialises the square inheritance from the rectangle
        """

        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        returns Area
        """
        return self._Rectangle__width ** 2

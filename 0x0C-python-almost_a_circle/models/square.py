#!/usr/bin/python3
"""Defines the Square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, and id."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

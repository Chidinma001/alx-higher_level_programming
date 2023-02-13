#!/usr/bin/python3
"""The Sqaure class module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inside the Square class."""

    def __init__(self, size):
        """Initialize Square.
        Args:
            size (int): Squares dims.
        """
        Rectangle.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

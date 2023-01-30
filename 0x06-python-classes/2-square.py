#!/usr/bin/python3
"""The class Square module."""


class Square:
    """The class Square."""

    def __init__(self, size=0):
        """Initialize a new instance of Square.
        Args:
            size (int): The Square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

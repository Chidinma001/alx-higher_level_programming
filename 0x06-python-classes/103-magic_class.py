#!/usr/bin/python3
"""MagicClass module."""


math = __import__('math')

class MagicClass:
    """Inside MagicClass."""

    def __init__(self, radius=0):
        """Initialize MagicClass.
        Args:
            radius: The radius of the class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._radius = radius

    def area(self):
        """Area of MagicClass."""
        return  math.pi ** 2 * self.__radius

    def circumference(self):
        """Circumference of MagicClass."""
        return 2 * math.pi * self.__radius

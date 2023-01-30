#!/usr/bin/python3
"""The class Square module."""


class Square:
    """The class Square."""

    def __init__(self, size=0):
        """Initialize a new instance of Square.
        Args:
            size (int): The Square size.
        """
        self.size = size

    def __eq__(self, other):
        """The equality dunder.
        Args:
            other (Square): The second instance of Square.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """The not equals dunder.
        Args:
            other (Square): The second instance of Square.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """The greater than dunder.
        Args:
            other (Square): The second instance of Square.
        """
        return self.area() > other.area()

    def __lt__(self, other):
        """The less than dunder.
        Args:
            other (Square): The second instance of Square.
        """
        return self.area() < other.area()

    def __ge__(self, other):
        """The greater than equals dunder.
        Args:
            other (Square): The second instance of Square.
        """
        return self.area() >= other.area()

    def __le__(self, other):
        """The less than eqals dunder.
        Args:
            other (Square): The second instance of Square.
        """
        return self.area() <= other.area()

    @property
    def size(self):
        """The private instance size getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """The private instance size setter.
        Args:
            value (int): The Square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This method calculate the area of Square."""
        return self.__size ** 2

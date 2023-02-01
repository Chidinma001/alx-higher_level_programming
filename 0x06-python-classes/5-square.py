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

    def my_print(self):
        """Print Squares."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                for _ in range(self.size):
                    print("{}".format("#"), end="")
                print()

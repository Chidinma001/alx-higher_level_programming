#!/usr/bin/python3
"""The class Square module."""


class Square:
    """The class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new instance of Square.
        Args:
            size (int): The Square size.
            position (Tuple(int, int)): Coords of square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Coords position getter."""
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        first, second = value

        if first < 0 or second < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method calculate the area of Square."""
        return self.__size ** 2

    def my_print(self):
        """Print Squares."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.size):
                for _ in range(self.__position[0]):
                    print(" ", end="")

                for _ in range(self.size):
                    print("{}".format("#"), end="")
                print()

    def __str__(self):
        """Str dunder."""
        if self.__size != 0:
            for _ in range(self.__position[1]):
                print()

        for _i in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            if _i != self.__size - 1:
                print()
        return ""

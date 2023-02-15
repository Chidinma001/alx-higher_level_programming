#!/usr/bin/python3
"""Empty BaseGeometry class."""


class BaseGeometry:
    """Inside the BaseGeometry class."""

    def area(self):
        """Area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator method.
        
        Args:
            name (str): str
            value (int): int
        Raises:
            TypeError and ValueError
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""The Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inside Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle.
        
        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

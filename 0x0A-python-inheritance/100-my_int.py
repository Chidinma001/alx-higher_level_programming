#!/usr/bin/python3
"""MyInt module."""


class MyInt(int):
    """MyInt inverts __eq__ and __ne__."""

    def __eq__(self, value):
        """Implement __ne__.
        
        Args:
            value (int): Check value.
        Returns:
            Boolean.
        """
        return self.real != value

    def __ne__(self, value):
        """Implement __eq__.
        
        Args:
            value (int): Check value.
        Returns:
            Boolean.
        """
        return self.real == value

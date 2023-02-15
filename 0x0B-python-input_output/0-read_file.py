#!/usr/bin/python3
"""The read_file.py module."""


def read_file(filename=""):
    """The read_file function.
    
    Args:
        filename (str): name of file.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        data = f.read()
        print(data, end="")

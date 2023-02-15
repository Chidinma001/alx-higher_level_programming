#!/usr/bin/python3
"""The write_file module."""


def write_file(filename="", text=""):
    """Inside the write_file func.
    
    Args:
        filename (str): name of file.
        text (str): write text to file.
    Returns:
        n (int): number of characters.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        n = f.write(text)
    return n

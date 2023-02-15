#!/usr/bin/python3
"""The write_file module."""


def append_write(filename="", text=""):
    """Inside the append_write func.
    
    Args:
        filename (str): file name.
        text (str): text to write.
    Returns:
        n (int): number of characters in text.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        n = f.write(text)
    return n

#!/usr/bin/python3

"""
add_integer
a function that adds two integers
"""
def add_integer(a, b=98):
    '''this works by adding two integers
    Args:
        a: the first variable not constant
        b: the constant or given variable to be 98 always
        Return: returns the mathematical sum of 'a' and 'b'
    
    '''
    if type(a) == float or type(b)  == float:
        a = int(a)
        b = int(b)
    if type(a) != int or type(b) != int:
        raise TypeError("a must be an integer")
    else:
        return a + b

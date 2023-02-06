#!/usr/bin/python3
'''
module for printing a square with th string '#'
'''
def print_square(size):
    '''
    
    :param size: the size that determines the size of the square
    :return: returns a sqaure the size of 'size'
    :raise: if size is less than 0, raise a ValueError, if size is not an integer and if size is a float
    '''
    if not isinstance(size, int):
       raise TypeError("size must be an integer")
    elif isinstance(size,(float)) and size <= 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        box = '#'
        print(box * size)
        print(end ='')

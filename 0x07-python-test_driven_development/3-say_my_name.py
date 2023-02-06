#!/usr/bin/python3
'''
module for saying names

'''
def say_my_name(first_name, last_name=""):
    '''
    
    :param first_name: the first name
    :param last_name: the last name
    :return: returns the full name  comprising of first and last name
     Raises:
        TypeError: If first_name or last_name is not a string
    
    '''

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name,str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

#!/usr/bin/env python3
'''
Module to do 'string stuff'
The goal is not to have students write complicated
functions; just create a wrapper for string methods
'''

def string_length( a_string ):
    '''
    Return the length of the argument string
    :param a_string: The string whose length we want
    :return: the length of the string
    '''
    return len( a_string )

def make_upper_case( a_string ):
    '''
    Return the upper case representation of the argument
    :param a_string: The string we want the upper case version of
    :return: a_string in upper case
    '''
    return a_string.upper()

def make_lower_case( a_string ):
    '''
    Return the lower case representation of the argument
    :param a_string: The string we want the lower case version of
    :return: a_string in lower case
    '''
    return a_string.lower()

def make_title_case( a_string ):
    '''
    Return the title case representation of the argument
    :param a_string: The string we want the title case version of
    :return: a_string in title case
    '''
    return a_string.title()

#if __name__ == "__main__":
    #main()
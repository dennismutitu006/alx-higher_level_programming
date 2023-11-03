#!/usr/bin/python3
def no_c(my_string):
    """This function will remove all characters c and from a string"""
    nCopy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(nCopy))

#!/usr/bin/python3
"""This module contains a function that adds numbers
"""


def add_integer(a, b=98):
    """This function adds two integers"""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if a >= 2 ** 62:
        raise OverflowError("a is too large")
    if b >= 2 ** 62:
        raise OverflowError("b is too large")
    if (a + b) >= (2 ** 62):
        raise OverflowError("result is too large")
    return a + b

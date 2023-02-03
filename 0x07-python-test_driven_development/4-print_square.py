#!/usr/bin/python3
"""This module contains the print square function
"""


def print_square(size):
    if type(size) == float:
        intsize = int(size)
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) == float and size == intsize:
        size = intsize
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i != size - 1:
            print("")

#!/usr/bin/python3
"""

This module defines a matrix division function

"""

def matrix_divided(matrix, div):
    """ The function divides all element of a matrix by a given number

    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for th division-integer or float
    Raises:
        TypeError: If the matrix contains non-members
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
    """

    if (

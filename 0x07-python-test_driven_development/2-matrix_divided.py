#!/usr/bin/python3
"""Matrix dividing module.
"""


def matrix_divided(matrix, div):
    """This gunction divides a mtrix."""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(type(i) == list for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(type(item) == float or type(item) == int for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    rowsz = len(matrix[0])
    for row in matrix:
        if len(row) != rowsz:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    numatrix = []
    for row in matrix:
        nurow = [round(i / 3, 2) for i in row]
        numatrix += [nurow]
    return numatrix

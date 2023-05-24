#!/usr/bin/python3
""" Module to find PEAK in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Arguments:
        list_of_integers(int)
    Return: None or Peak.
    """
    size = len(list_of_integers)
    mid_el = size
    midd = size // 2

    if size == 0:
        return None

    while True:
        mid_el = mid_el // 2
        if (midd < size - 1 and
                list_of_integers[midd] < list_of_integers[midd + 1]):
            if mid_el // 2 == 0:
                mid_el = 2
            midd = midd + mid_el // 2
        elif mid_el > 0 and list_of_integers[midd] < list_of_integers[midd - 1]:
            if mid_el // 2 == 0:
                mid_el = 2
            midd = midd - mid_el // 2
        else:
            return list_of_integers[midd]

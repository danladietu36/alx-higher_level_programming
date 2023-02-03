#!/usr/bin/python3
"""This module contains the indentation function
"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for l in text:
        print(l, end="")
        if l == "." or l == "?" or l == ":":
            print("\n")

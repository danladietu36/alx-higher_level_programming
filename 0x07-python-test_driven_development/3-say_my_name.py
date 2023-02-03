#!/usr/bin/python3
"""This module prints a name
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    if first_name != "" and last_name != "":
        print("My name is {:s} {:s}".format(first_name, last_name))
    elif first_name == "" and last_name == "":
        print("Name not given")
    elif first_name == "":
        print("My Last name is {:s}".format(last_name))
    else:
        print("My First name is {:s}".format(first_name))

#!/usr/bin/python3
"""Module for the method add_attribute"""


def add_attribute(obj, name, value):
    """Method for checking and adding new attribute"""

    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

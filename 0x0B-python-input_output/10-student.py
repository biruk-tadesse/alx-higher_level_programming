#!/usr/bin/python3
""" Program that defines a Student using filter """


class Student:
    """ class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        dic = {}
        if (type(attrs) is not list):
            return (self.__dict__)
        else:
            for i in attrs:
                if (i in self.__dict__):
                    dic[i] = self.__dict__[i]
            return (dic)
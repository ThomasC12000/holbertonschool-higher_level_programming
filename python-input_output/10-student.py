#!/usr/bin/python3
'''MODULE'''


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with their first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the student instance"""
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

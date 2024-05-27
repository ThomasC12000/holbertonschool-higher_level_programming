#!/usr/bin/python3
'''MODULE'''


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with their first name, last name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

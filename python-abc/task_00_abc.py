#!/usr/bin/python3
"""Module for the abstract class"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """parent class Animal"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """class dog inherits from the Animal class"""
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    """class Cat inherits from the Animal class"""
    def sound(self):
        return "Meow"

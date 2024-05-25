#!/usr/bin/env python3
'''Module for Shape'''
from abc import ABC, abstractmethod
from math import pi
'''module for class Shape'''


class Shape(ABC):
    '''shape class'''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    '''class circle that inherits from Shape'''
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    '''class Rectangle that inherits from Shape'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

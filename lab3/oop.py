"""
3-Create a Vehicle class without any variables and methods
"""

# class Vehicle:
#     pass


"""
4-Create a Vehicle class with max_speed and mileage instance attributes
"""


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


"""
6-Write a Python class which has two methods get_String and print_String. get_String 
accept a string from the user and print_String print the string in upper case
"""


class ShowString:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Enter a string: ")

    def print_String(self):
        print(self.s.upper())


""""
7-Write a Python class named Circle constructed by a radius and two methods which will 
compute the area and the perimeter of a circle. 
"""
import math


class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return self.r**2 * math.pi

    def perimeter(self):
        return 2 * self.r * math.pi

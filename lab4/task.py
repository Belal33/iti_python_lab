"""
1- Define a class attribute”color” with a default value white. I.e., Every Vehicle should be
        white.
"""

# class Vehicle:
# 	color = "White"
# 	def __init__(self, name, max_speed, mileage):
# 		self.name = name
# 		self.max_speed = max_speed
# 		self.mileage = mileage

# class Bus(Vehicle):
# 	pass
# class Car(Vehicle):
#     pass

"""
2- Create a Bus child class that inherits from the Vehicle class. The default fare charge of
any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra
10% on full fare as a maintenance charge. So total fare for bus instance will become the
final amount = total fare + 10% of the total fare.

Note:​
	The bus seating capacity is 50. so the final fare amount should be 5500. You need
	to override the fare() method of a Vehicle class in Bus class.
Use the following code for your parent Vehicle class. We need to access the parent class
from inside a method of a child class.
"""


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 0.1
        return amount


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


"""
3- Determine if School_bus is also an instance of the Vehicle class
"""
# print(isinstance(School_bus, Vehicle))

"""
	4-Define a class named Rectangle which can be constructed by a length and width. The
	Rectangle class has a method which can compute the area.
Hints:
	Use def methodName(self) to define a method.
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


"""
5- Define a class which has at least two methods:
	getString: to get a string from console input
	printString: to print the string in upper case.
"""


class stringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


"""
6-Define a class Person and its two child classes: Male and Female. All classes have a
method "getGender" which can print "Male" for Male class and "Female" for Female
class.
"""


class Person:
    def getGender(self):
        pass


class Male(Person):
    def getGender(self):
        print("Male")


class Female(Person):
    def getGender(self):
        print("Female")


"""
7- Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid
but "[)", "({[)]" and "{{{" are invalid
"""


class ParenthesesValidator:
    def __init__(self, string):
        self.string = string

    def is_valid(self):
        brackets = {")": "(", "}": "{", "]": "["}
        opened = []
        for char in self.string:
            if char in brackets.values():
                opened.append(char)
            elif char in brackets.keys():
                if brackets[char] == opened[-1]:
                    opened.pop()
                else:
                    return False
        return opened == []


# Example usage:
validator = ParenthesesValidator("((){[]}{})")
print(validator.is_valid())  # Output: True

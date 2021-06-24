Functional Calculator
Timings
30 - 60 Minutes

Summary
Amazing you now know functions, lets make a functional calculator.

Tasks
Complete the core tasks
`python

Create a class called Calculator
functions
practice using, defining and calling functions
Build a basic functional
Core 1: build function containing
# add,
# subtract,
# multiply,
# divide.
`class Calculator:
    def add(self,num1,num2):
        return num1 + num2
    def subtract(self,num1,num2):
        return num1 - num2
    def divide(self,num1,num2):
        return num1 / num2
    def multiply(self,num1,num2):
        return num1 * num2
test = Calculator()`

`print(test.add(1,3))
print(test.subtract(5,1))
print(test.divide(4,2))
print(test.multiply(5,2))`
## Create a file for child class called Functional_calculator import calculator class and inherit all the functionality Core 2: Build more functions for
# area of a circle
# area of a square
# area of a triangle (just find the easiest way)


`from calculator import Calculator
import math`

`class functionalcalc(Calculator):
    def __init__(self):
        super().__init__()
    def area_circle(self, radius):
        return math.pi * (radius ** 2)
    def area_square(self, length, width):
        return self.multiply(length, width)
    def area_triangle(self, base, height):
        return .5 * self.multiply(base, height)
area = functionalcalc()`

`print(area.area_circle(10))
print(area.area_square(2, 10))
print(area.area_triangle(4, 10))`


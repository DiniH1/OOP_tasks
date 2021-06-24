
from calculator import Calculator
import math

class functionalcalc(Calculator):
    def __init__(self):
        super().__init__()
    def area_circle(self, radius):
        return math.pi * (radius ** 2)
    def area_square(self, length, width):
        return self.multiply(length, width)
    def area_triangle(self, base, height):
        return .5 * self.multiply(base, height)

area = functionalcalc()

print(area.area_circle(10))
print(area.area_square(2, 10))
print(area.area_triangle(4, 10))
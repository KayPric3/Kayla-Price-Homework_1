# Write a Python class named Circle constructed by a radius and two methods that will compute the
# area and the perimeter of a circle.
import math
class Circle():
    def __init__(self,r):
        self.radius = r
    def area(self):
        return self.radius * self.radius * math.pi
    def perimeter(self):
        return 2 * math.pi * self.radius

circle1 = Circle(3)
print("Area: ", round(circle1.area(),3))
print("Perimeter: ", round(circle1.perimeter(),3))

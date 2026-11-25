# Topic 12, Task 3: Shape Area Calculator

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2      # Area 


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width        # Area 


circle = Circle(7)
rectangle = Rectangle(10, 5)

print(f"Area of circle (radius 7): {circle.area():.2f}")
print(f"Area of rectangle (10 x 5): {rectangle.area():.2f}")

print()
print("Explanation: Circle and Rectangle both implement area(), but with")
print("different formulas. Code can call shape.area() on any Shape without")
print("knowing its exact type - that is polymorphism.")
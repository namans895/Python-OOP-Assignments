# Shape Area Calculator using Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Creating object
r1 = Rectangle(10, 5)

print("Area of Rectangle =", r1.area())

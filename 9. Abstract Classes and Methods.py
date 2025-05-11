from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(Self):
        pass

class Rectangle(Shape):
    def __init__(self, lenght, widht):
        self.length = lenght
        self.widht = widht

    def area(Self):
        return Self.length * Self.widht

r1 = Rectangle(10, 20)
print(r1.area())
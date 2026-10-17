from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius:int) -> None:
        self.radius:int = radius
        self.pi = 3.14

    def area(self):
        print(f"area is: {self.pi * self.radius * self.radius} cm sq")

    def perimeter(self):
        print(f"perimeter is: {self.pi * self.radius * 2} cm")
    
    
c = Circle(10)
c.area()
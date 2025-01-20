import math

class Calculator:
    
    @staticmethod
    def add(a:int, b:int) -> int:
        return a + b
    
    
class Counter:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1
        
# Counter.increment()
# Counter.increment()
# print(Counter.count)

class circle:
    
    def __init__(self, radius:float):
        self._radius = radius
        
    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value:float):
        if value < 0:
            raise ValueError("El radio debe se positivo")
        
        self._radius = value
    
circle = circle(5)

print(circle.area)

circle.radius = 10

print(circle.area)
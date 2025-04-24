# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

# Importing abc built-in module
from abc import abstractmethod, ABC

# Create shape class with inherit from ABC
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Create Rectangle class with inherit from shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Multiply the area
    def area(self):
        return self.width * self.height

# Store values
rect = Rectangle(5,10)

# Print data
print(f"Area of Rectangle is: {rect.area()}")
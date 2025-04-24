# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand # Public method
    
    def start(self): # Public method
        return f"{self.brand}"
    
my_car = Car("Toyota")

print(my_car.brand)

print(my_car.start())

# Output: 
# Toyota
# Toyota
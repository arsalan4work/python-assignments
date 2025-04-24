# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition 
# by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        return f"The {self.engine_type} engine is starting"

class Car(Engine):
    def __init__(self, brand, engine):
        self.brand = brand
        # Composition: Passing an engine object to the car class
        self.engine = engine
    
    def start_car(self):
        # access the start method of the engine class
        return f"{self.brand} car is starting. {self.engine.start()}"

# Engine object
engine = Engine("V8")

# Car object
car = Car("Ford", engine)

# Calling the start_car method which uses the engine start method
print(car.start_car())

# Output: Ford car is starting. The V8 engine is starting
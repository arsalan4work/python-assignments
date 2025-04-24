# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

# Create class Dog
class Dog:
    def __init__(self, name, breed):
        # Instances Variable
        self.name = name
        self.breed = breed
    
    def bark(self):
        # Instance method that prints a message with dog's
        return f"{self.name} says woof!!"
    
# Store data
dog = Dog("Jolly", "German Shepherd")
print(dog.bark()) # Calling Bark

# Output: Jolly says woof!!
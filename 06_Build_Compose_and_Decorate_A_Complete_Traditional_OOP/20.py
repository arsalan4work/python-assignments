# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older")
    else:
        print(f"Age {age} is valid!")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integar for age")
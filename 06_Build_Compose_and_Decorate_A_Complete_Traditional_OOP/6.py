# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:

    # Constructor
    def __init__(self):
        print("Logger object has been created!")
    
    # Destructor
    def __del__(self):
        print("Logger object has been destroyed!")
    
# Create an object of logger class
logger = Logger()

# Delete the object explicitly to invoke the destructor
del logger

# Output: 
# Logger object has been created!
# Logger object has been destroyed!
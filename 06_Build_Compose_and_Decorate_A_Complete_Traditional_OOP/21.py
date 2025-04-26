# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
import time

class CountDown:
    def __init__(self, start):
        self.start = start # Set the starting number
        self.current = start # Initializing current to the starting number

    def __iter__(self):
        # Returns the iterator ibject it self
        return self
    
    def __next__(self):
        # If current is less than 0 stop iteration
        if self.current < 0:
            raise StopIteration
        # Decrease current by 1 and return the value
        self.current -= 1
        return self.current + 1 # Returns the number before decrementing

# Creating object
countdown = CountDown(5)

# Using the countdown object in for loop
for number in countdown:
    time.sleep(1)
    print(number)
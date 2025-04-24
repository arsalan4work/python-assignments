# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable 
# and a class method with cls to manage and display the count.

class Counter:
    count = 0 #initialze value
    def __init__(self):
        Counter.count += 1 # adding value
    
    # Class method to update class
    @classmethod
    def get_count(cls):
        return cls.count # here we are adding values to class variable get_count()
    
c1 = Counter()
c2 = Counter()
c3 = Counter()

print(c3.get_count())

# Output: 3 because we created 3 classes above
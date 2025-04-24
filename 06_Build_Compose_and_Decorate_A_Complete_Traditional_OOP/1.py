# 1. Using self 
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values 
# via a constructor. Add a method display() that prints student details.



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"Student name is {self.name}, Student marks in Computer Science is {self.marks}"

std = Student("Arsalan", "98")
print(std.display())

# Output: Student name is Arsalan, Student marks in Computer Science is 98
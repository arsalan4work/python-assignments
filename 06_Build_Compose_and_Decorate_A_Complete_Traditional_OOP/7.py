# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# - a public variable name,

# - a protected variable _salary, and

# - a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:

    def __init__(self, name, salary, ssn):
        self.name = name # Public Variable
        self._salary = salary # Protected Variable
        self.__ssn = ssn # Private Variable

# Store values
employee = Employee("Arsalan", 5000, 12345678)
# Public variable will be shown
print(employee.name)

# Protected variable will also shown 
print(employee._salary)


try:
    # Here private variable is not shown
    print(employee.__ssn)
except AttributeError as ae:
    print(f"Error: {ae}")

# This is the way to access private variables via mangling
print(employee._Employee__ssn)

# Output: 
# Arsalan
# 5000
# Error: 'Employee' object has no attribute '__ssn'
# 12345678
# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department 
# object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_employee_info(self):
        return f"Employee Name: {self.name}, Position: {self.position}"
    
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        # Aggregation: Storing a reference to an employee object
        self.employee = employee

    def get_department_info(self):
        return f"Department: {self.department_name}, Employee: {self.employee.get_employee_info()}"
    
# creating an employee object
employee1 = Employee("Arsalan", "Software Engineer")

# creating a department  object and pass the employee object to it
department1 = Department("IT Department", employee1)

# calling the method to get the department and employee info
print(department1.get_department_info())

# Output: Department: IT Department, Employee: Employee Name: Arsalan, Position: Software Engineer
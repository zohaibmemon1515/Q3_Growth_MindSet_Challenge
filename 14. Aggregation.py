class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, emp):
        self.emp = emp

emp = Employee("Zohaib")
dept = Department(emp)
print(dept.emp.name)
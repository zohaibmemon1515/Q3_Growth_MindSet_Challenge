class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

e1 = Employee("Zohaib", 50000, "123-234-654")
print(e1.name)
print(e1._salary) # Print but not recommended
# print(e1.__ssn) # Error
print(e1._Employee__ssn) #name mangling

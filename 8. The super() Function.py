class Person:
    def __init__(self, name):
        self.name = name


class teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t1 = teacher("Zohaib", "Ai")
print(t1.name, t1.subject)
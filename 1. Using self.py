class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Your name is {self.name}, and you obtained {self.marks} marks.")
    
S1 = Student("Zohaib", 90)
S1.display()
        
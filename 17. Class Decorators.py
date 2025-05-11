def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decoraters!"
    return cls

@add_greeting
class person:
    def __init__(self, name):
        self.name = name

p = person("Zohaib")
print(p.greet())
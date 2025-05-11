class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is Barking!")
    
d1 = dog("Kelly", "LOnger")
d1.bark()
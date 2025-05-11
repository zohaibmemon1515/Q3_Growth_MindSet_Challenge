class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car has started.")

C1 = Car("Toyota")
print(C1.brand)
C1.start()          
class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price
    

    @price.setter
    def price(self, value):
        if value < 0 :
            raise ValueError("Price cannot be negative!")
        self._price = value

p1 = Product()
p1.price = 100
print(p1.price)


class Book:
    total_book = 0

    def __init__(self):
        Book.increment_count()

    @classmethod
    def increment_count(cls):
        cls.total_book += 1

print(Book.total_book)
b1 = Book
b2 = Book
print(Book.total_book)
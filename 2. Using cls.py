class Counter:
    counter = 0

    def __init__(self):
        Counter.counter += 1
        
    @classmethod
    def show_count(cls):
        print(f"You should created {cls.counter} objects.")

C1 = Counter()
C2 = Counter()

Counter.show_count()
class Engine:
    def start(self):
        print("Engine Started!")

class Car():
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

e1 = Engine()
C = Car(e1)
C.start()
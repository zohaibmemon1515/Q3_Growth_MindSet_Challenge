class Logger:
    def __init__(self):
        print("Logger Object Created!")
    def __del__(self):
        print("Logger Object Destroy!")

L1 = Logger()
del L1
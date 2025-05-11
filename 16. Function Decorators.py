def log_function_call(func):
    def wrapper():
        print("Function is Being Called!")
        func()
        print("After Function Called!")
    return wrapper

@log_function_call
def say_hello():
    print("Hello World")

say_hello()
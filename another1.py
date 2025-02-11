def my_decorator(func):
    def wrapper(*args):
        print("Before calling the function")
        result = func(*args)
        print("After calling the function")
        return result
    return wrapper

@my_decorator   # greet = my_decorator(greet)
def greet(name):
    print("Hello, " + name + "!")


greet("Alice")
import functools

class Counter():
    def __init__(self, initial = 0):
        self.__counter = initial
    
    def reset(self):
        self.__counter = 0

    def get(self):
        return self.__counter

    def increment(self):
        self.__counter += 1

def make_counter(initial = 0):
    class Decorator():
        def __init__(self, func):
            self.counter = Counter(initial)
            self.__func = func

        def __call__(self, *args, **kwargs):
            self.counter.increment()
            return self.__func(*args, **kwargs)


    return Decorator

def make_counter(initial = 0):
    counter = initial
    def decorator(func):
        def wrapper(*args, **kwargs):
            counter += 1 
            return func(*args, **kwargs)

        return wrapper
    return decorator

@make_counter(initial = 10)
def say_hello(a):
    return "Hello there", a
    
print(say_hello("a"))
print(say_hello.counter.get())
#print(say_hello())
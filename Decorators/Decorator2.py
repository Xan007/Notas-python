import functools

def uppercase_decorator(func):
    @functools.wraps(func) #Esto hace que no se pierda la meta data.
    #Ayuda a debuguear mejor.
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def say_hi():
    "This will say hi"
    return 'hello there'

print(say_hi())
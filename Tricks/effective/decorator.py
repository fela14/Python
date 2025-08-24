def null_decorator(func):
    return func

def greet():
    return 'Hello'

my_greet = null_decorator(greet)
print(my_greet())

@null_decorator
def greet():
    return 'hello'

print(greet())

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    return 'hello world'

print(greet())

print(greet)
print(null_decorator)
print(uppercase(greet))
    
def scream(func):
    def wrapper():
        return func().upper() + '!!!'
    return wrapper

@scream
def speak():
    return 'hello python'
print(speak())

def para(func):
    def wrapper():
        return '<p>' + func() + '</p>'
    return wrapper
def strong(fun):
    def wrapper():
        return '<strong>' + fun() + '</strong>'
    return wrapper
def emphasis(fu):
    def wrapper():
        return '<em> ' + fu() + ' </em>'
    return wrapper

@para
@strong
@emphasis
def greet():
    return 'Hello world'
print(greet())
        

def trace(func):
    def wrapper(*args, **kwargs):
        print(f"TRACE calling {func.__name__}()"
              f" with {args} {kwargs}")
        original_result = func(*args, **kwargs)
        print(f"TRACE: {func.__name__}()"
              f" with {original_result!r}")
        return original_result
    return wrapper
@trace
def say(name, line):
    return f"{name}: {line}"

print(say("Alice", "Hello world"))

def greet():
    """Return a friendly greeting."""
    return "Hello"
decorated_greet = uppercase(greet)

print(greet.__name__)
print(greet.__doc__)
print(decorated_greet.__name__)
print(decorated_greet.__doc__) 

import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper
@uppercase
def greet():
    """Return a friendly greeting."""
    return "Hello"
print(greet.__name__)
print(greet.__doc__)

# --- *args and **kwargs ---

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
foo('money')
print(foo('money', 1,2,3))
print(foo('money', 1,2,3, key1='result', key2=999))

def bar(x, *args, **kwargs):
    print(f'x: {x}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
def foo(x, *args, **kwargs):
    kwargs['Alice'] = 'Bob'
    new_args = args + ('extra',)
    bar(x, *new_args, **kwargs)

foo('hello', 1,2,3, key='value')

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage  

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

a = AlwaysBlueCar('green', 8282)
print(a.color)
print(a.mileage)

import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func, args, kwargs)
        result = func(*args, **kwargs)
        print(result)
    return wrapper

@trace
def speak(greet, name):
    return '{}, {}!'.format(greet, name)

speak('Hello', 'Bob')







    
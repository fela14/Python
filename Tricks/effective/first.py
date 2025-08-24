def yell(text):
    return text.upper() + '!'
print(yell('hello'))

bark = yell
print(bark('woof'))

del yell
# yell('hello')

print(bark('hey'))
print(bark.__name__)

funcs = [bark, str.lower, str.upper, str.capitalize]
print(funcs)
for f in funcs:
    print(f, f('hElLo'))
print(funcs[0]('hey there'))

def greet(fun):
    greeting = fun('hEy tHeRe, i aM a pYtHoN pRoGrAm')
    print(greeting)
funcs = [bark, str.lower, str.upper, str.capitalize]
for f in funcs:
    greet(f)

def whisper(text):
    return text.lower() + '...'
print(whisper('hEy tHeRe, i aM a pYtHoN pRoGrAm'))

loud = list(map(bark, ['hello', 'hey', 'hi']))
print(loud)

def speak(text):
    def whisp(t):
        return t.lower() + '...'
    return whisp(text)

print(speak('HELLO WORLD'))
# print(whisp('HELLO WORLD'))    # NameError: name 'whisp' is not defined.

def speak(num):
    def whisp(t):
        return t.upper() + '!'
    def yell(t):
        return t.lower() + '...'
    if num > 0:
        return whisp
    else:
        return yell
    
print(speak(-1))
print(speak(1))

speak_fun1 = speak(-4)
speak_fun2 = speak(4)
print(speak_fun1('mOnTy'))
print(speak_fun2('mOnTy'))

def speak(text, num):
    def whisp():
        return text.lower() + '...'
    def yell():
        return text.lower() + '!'
    if num > 0:
        return whisp
    else:
        return yell
    
x = speak('Hello world', 0.7)()
y = speak('Hello world', -0.7)()
print(x)
print(y)

def make_adder(n):
    def add(x):
        return x + n
    return add
plus_3 = make_adder(3)
print(plus_3(4))
print(plus_3(6))

class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x
plus_3 = Adder(3)
print(plus_3(5))

print(callable(plus_3))
print(callable(greet))
print(callable(speak))
print(callable(whisper))
print(callable(bark))




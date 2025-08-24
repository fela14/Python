errno = 50159747054
name = 'Bob'
a = 5
b = 10

#1 - "Old Style" String Formatting

print("Hello %s" % (name))
print('%x' % errno)
print("Hey %s, there is a 0x%x error" % (name, errno))
print("Hey %(name)s, there is a 0x%(errno)x error" % {'name': name, 'errno': errno})

#2 - "New Style" String Formatting

print("Hello {}".format(name))
print("Hey {name}, there is a 0x{errno:x} error".format(name=name, errno=errno))

#3 - Literal String Interpolation

print(f'Hello, {name}!')
print(f'Five plus ten is {a+b} and not {2*(a+b)}')

def greeting(name, question):
    return f'Hello {name}, how is it {question}?'

print(greeting('Bob', 'going'))

def greeting(name, question):
    return f'Hello ' + name + ', ' + 'how is it ' + question + '?'

print(greeting('Bob', 'going'))

import dis

dis.dis(greeting)

print(f'Hey {name}, there is a {errno:#x} error!')

#4 - Template Strings

from string import Template

x = Template('Hey $name1')
greet = x.substitute(name1=name)
print(greet)
x = Template('Hello $name. there is a $errno error')
error = x.substitute(name=name, errno=hex(errno))
print(error)

SECRET = 'this-is-a-secret'
class Error:
    def __init__(self):
        pass
err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'

print(user_input.format(error=err))

user_input = '${error.__init__.__globals__[SECRET]}'
# Template(user_input).substitute(error=err)    # ValueError: Invalid placeholder in string: line 1, col 1
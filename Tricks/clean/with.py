with open('hello.txt', 'a') as f:
    f.write('hello, world\n')

f = open('hello.txt', 'a')
f.write('another hello, world\n')
f.close()

class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'a')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hi.txt') as f:
    f.write('hi')

from contextlib import contextmanager

@contextmanager
def ManagedFile(name):
    try:
        f = open(name, 'a')
        yield f
    finally:
        f.close()

with ManagedFile('hey.txt') as f:
    f.write('hey')




class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)

with Indenter() as indent:
    indent.print('Hi')
    with indent:
        indent.print('Hey')
        with indent:
            indent.print("Bonjour")
    indent.print('Hi')
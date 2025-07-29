numbers = [1,2,3]
for n in numbers:
    print(n)

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)
    
class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    
    def __next__(self):
        return self.source.value
    
repeater = Repeater('Hello')
# for item in repeater:
#     print(item)

# iterator = repeater.__iter__()
# while True:
#     item = iterator.__next__()
#     print(item)

iterator = iter(repeater)
print(next(iterator))
print(next(iterator))
print(next(iterator))

class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value
    
repeater = Repeater('Hello')
# for item in repeater:
#     print(item)
print("*"*25)
class BoundedRepeater:
    def __init__(self, value, max_repeat):
        self.value = value
        self.max_repeat = max_repeat
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.max_repeat:
            raise StopIteration
        self.count += 1
        return self.value
    
repeater = BoundedRepeater('Hello', 3)
# for item in repeater:
#     print(item)
iterator = iter(repeater)
while True:
    try:
        item = next(repeater)
    except StopIteration:
        break
    print(item)
print('+'*25)

# --- Generators ---

def repeater(value):
    while True:
        yield value

# for x in repeater('Hi'):
#     print(x)

iterator = repeater('Hi')
print(next(iterator))
print(next(iterator))
print(next(iterator))

print('#'*25)

def repeat_three_times(value):
    yield value
    yield value
    yield value
for x in repeat_three_times('Hi'):
    print(x)

def Bounded(value, max):
    count = 0
    while True:
        if count >= max:
            return
        count += 1
        yield value

for x in Bounded('Bound', 5):
    print(x)

iterator = ('Hello' for x in range(3))
for i in iterator:
    print(i)
        
def B_iter(value, max):
    for i in range(max):
        yield value
b_iter = B_iter('bb', 3)
for i in b_iter:
    print(i)

list_comp = ['Hello' for i in range(3)]
gen_comp = ('Holla' for i in range(3))
print(list_comp)
print(gen_comp)
print(next(gen_comp))
print(next(gen_comp))
print(next(gen_comp))

even_squares = (x*x for x in range(10) if x%2==0)
for x in even_squares:
    print(x)

for x in ('Bombom' for x in range(8)):
    print(x)



    
        
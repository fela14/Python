phonebook = {
    'bob': 7387,
    'alice': 3719,
    'jack': 7052
}

squares = {x: x*x for x in range(6)}

print(phonebook['alice'])
print(squares)

from collections import OrderedDict, defaultdict, ChainMap

# --- OrderedDict ---

d = OrderedDict(one=1, two=2, three=3)
print(d)
d['four'] = 4
print(d)
print(d.keys())
print(d.values())

# --- DefaultDict ---

dd = defaultdict(list)
dd['dogs'].append('rufus')
dd['dogs'].append('james')
dd['dogs'].append('kitty')
print(dd['dogs'])

my_dict = defaultdict(dict)
my_dict['user1']['name'] = 'rufus'
my_dict['user1']['age'] = 24
my_dict['user2']['name'] = 'june'
my_dict['user2']['age'] = 49
my_dict['user3']['name'] = 'kitty'
my_dict['user3']['age'] = 92
print(my_dict)
print(my_dict['user1'])
print(my_dict['user2'])
print(my_dict['user3'])

ss = defaultdict(set)
ss['cat'].add('rufus')
ss['cat'].add('james')
ss['cat'].add('kitty')
print(ss['cat'])

# --- ChainMap ---
dict1 = {'name': 'james', 'age': 46}
dict2 = {'nick': 'killings', 'num': 29}
chain = ChainMap(dict1, dict2)
print(chain)
print(chain['name'])
print(chain['nick'])

from types import MappingProxyType

writable = {'name': 'james', 'age': 46}
read_only = MappingProxyType(writable)

print(read_only)
# read_only['nick'] = 'killings'
print(read_only)    #'mappingproxy' object does not support item assignment
writable['nick'] = 'killings'
print(read_only)

writable = {'age': 89, 'sch': 'hope high'}
read_only = MappingProxyType(writable)
print(read_only)
#read_only['bday'] = 'April 16'
print(read_only)
writable['bday'] = 'April 16'
print(read_only)

# --- Arrays ---

arr = ['one', 'two', 'three']
print(arr)
print(arr[0])
arr[1] = 'hello'
print(arr)
del arr[1]
print(arr)
arr.append('holla')
print(arr)

# --- Tuples ---

arr = 'one', 'two', 'three'
print(arr[0])
print(type(arr))
# arr[1] = 'hello'    # 'tuple' object does not support item assignment
print(arr)
# del arr[1]          # 'tuple' object doesn't support item deletion
arr = arr + ('four', 'five',)
print(arr)

import array

arr = array.array('f', (2.3, 3.5, 45.5, 46,4))
print(arr)
print(arr[0])
print(arr[1])
# arr[1] = 'hello'   # must be real number, not str

arr = array.array('i', (2,3,4,5,6))
print(arr)
print(arr[0])
print(arr[1])
print(arr[3])
# arr[1] = 4.0       # 'float' object cannot be interpreted as an integer
print(arr[1])

arr = 'bcde'
print(arr[1])
# del arr[1]        # 'str' object doesn't support item deletion
print(arr[1])

my_list = list('abcde')
print(my_list)
my_string = ''.join(my_list)
print(my_string)

arr = bytes((1,2,3))
print(arr[2])
# brr = bytes((0,299))    # ValueError: bytes must be in range(0, 256)
print(arr[0])
# del arr[2]              # TypeError: 'bytes' object doesn't support item deletion
# arr[1] = 26             # TypeError: 'bytes' object does not support item assignment
print(arr[1])
print(arr)

arr = bytearray((1,2,3))
print(arr)
arr[1] = 23
print(arr[1])
del arr[1]
print(arr)
arr.append(34)
print(arr)
# arr[2] = 777            # ValueError: byte must be in range(0, 256)
print(arr)
# arr[1] = 'hello'        # TypeError: 'str' object cannot be interpreted as an integer
print(arr)                

car1 = {
    'color': 'red',
    'mileage': 23.3,
    'automatic': True
}
car2 = {
    'color': 'blue',
    'mileage': 523.39,
    'automatic': False
}
print(car1)
print(car2)
print(car2['mileage'])

class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

car1 = Car('red', 824.2, True)
car2 = Car('black',20938.2, False)
print(car1.color)
print(car2.mileage)

from collections import namedtuple
from sys import getsizeof

p1 = namedtuple('Point', 'x y z')(1, 2, 3)
p2 = (1, 2, 3)

print(getsizeof(p1))
print(getsizeof(p2))

Car = namedtuple('Car', 'color mileage, automatic')
car1 = Car('black', 20938.2, False)
print(car1)
print(car1.mileage)

from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car3 = Car('black', 20938.2, False)
# Type annotations are not enforced without 
# a separate type checking tool like mypy
car4 = Car('black','NOT_A_FLOAT', False) 
print(car3)
print(car3.mileage)
print(car4)
print(car4.mileage)

from struct import Struct

my_data = Struct('i?f')
data = my_data.pack(23,False,44.4)
print(data)
u_data = my_data.unpack(data)
print(u_data)

from types import SimpleNamespace

car1 = SimpleNamespace(color='red',
                       mileage=34,
                       automatic='False')
print(car1)
print(car1.color)
del car1.automatic
print(car1)

# --- sets and multisets ---

vowels = {'a', 'e', 'i', 'o', 'u'}
print('e' in vowels)

letters = set('alice')
print(letters)

print(letters.intersection(vowels))

vowels.add('x')
print(vowels)

vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# vowels.add('d')     # AttributeError: 'frozenset' object has no attribute 'add'
print(vowels)

vowels_dict = {frozenset({'a', 'e', 'i', 'o', 'u'}): 'my_dict'}
print(vowels_dict)
print(vowels_dict[frozenset({'a', 'e', 'i', 'o', 'u'})])


from collections import Counter

inventory = Counter()
loot = {'goods': 0, 'toys': 7}
inventory.update(loot)
print(inventory)
more_loot = {'goods': 10, 'toys': 37}
inventory.update(more_loot)
print(inventory)
print(len(inventory))
print(sum(inventory.values()))

# --- Stacks(LIFOs) ---

s = []
s.append('toy')
s.append('goods')
s.append('money')
print(s)

print(s.pop())
print(s.pop())
print(s.pop())
print(s)

from collections import deque

s = deque()
s.append('dog')
s.append('cat')
s.append('sleep')
print(s)
print(s.pop())
print(s.pop())
print(s.pop())

from queue import LifoQueue

s = LifoQueue()
s.put('life')
s.put('o')
s.put('queue')
print(s)
print(s.get())
print(s.get())
print(s.get())
print(s)
# print(s.get_nowait())

# --- Queues(FIFOs) ---

q = []
q.append('cry')
q.append('baby')
q.append('cody')
print(q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

from collections import deque

q = deque()
q.append('ewa')
q.append('ade')
q.append('shushu')
print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)

from queue import Queue

q = Queue()
q.put("bouncing")
q.put("baby")
q.put("boy")
print(q)
print(q.get())
print(q.get())
print(q.get())

from multiprocessing import Queue

q = Queue()
q.put("bouncing")
q.put("baby")
q.put("boy")
print(q)
print(q.get())
print(q.get())
print(q.get())

# --- Priority Queue ---

q = []

q.append((1, 'bouncing'))
q.append((0, 'baby'))
q.append((4, 'boy'))
q.append((2, 'and'))
q.append((3, 'girl'))

q.sort(reverse=True)

for i in range(5):
    next_item = q.pop()
    print(next_item)

from heapq import heappush, heappop

q = []

heappush(q, (1, 'bouncing'))
heappush(q, (0, 'baby'))
heappush(q, (4, 'bouncing'))
heappush(q, (2, 'boy'))
heappush(q, (3, 'girl'))

for i in range(len(q)):
    x = heappop(q)
    print(x)

from queue import PriorityQueue

q = PriorityQueue()

q.put('simple')
q.put('answers')
q.put('only')

while not q.empty():
    next_item = q.get()
    print(next_item)





class TheSimplestClass:
    pass
my_first_object = TheSimplestClass()

stack = []
def push(val):
    stack.append(val)
def pop():
    val = stack[-1]
    del stack[-1]
    return val
push(3)
push(2)
push(1)
print(pop())
print(pop())
print(pop())

class Stack():
    def __init__(self):
        print('Hi')
stack_obj = Stack()

class Stack():
    def __init__(self):
        self.stack_list = []
        self.__stack_list = []

stack_obj = Stack()
print(len(stack_obj.stack_list))
# print(len(stack_obj.__stack_list)) # AttributeError

class Stack():
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_obj = Stack()

stack_obj.push(3)
stack_obj.push(2)
stack_obj.push(1)
print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())

stack_obj_1 = Stack()
stack_obj_2 = Stack()

stack_obj_1.push(3)
stack_obj_2.push(stack_obj_1.pop())
print(stack_obj_2.pop())

little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)
print(funny_stack.pop())

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def get_sum(self):
        return self.__sum
    
print()

# The Stack

class Stack():
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum
    
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
stack_obj = AddingStack()

for i in range(5):
    stack_obj.push(i)
print(stack_obj.get_sum())

for i in range(5):
    print(stack_obj.pop())

# Counting Stack

class Stack():
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
class CountStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter
    
    def pop(self):
        self.__counter += 1
        return Stack.pop(self)

stk = CountStack()

for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())


# Queue aka FIFO

class QueueError(IndexError):
    pass

class Queue():
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) > 0:
            elem = self.__queue[-1]
            del self.__queue[-1]
            return elem
        else:
            raise QueueError
        
que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

# Queue aka FIFO: Part 2

class QueueError(IndexError):
    pass

class Queue():
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            return QueueError
        
class SuperQueue():
    def isempty(self):
        return len(self.queue) == 0
    
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        if not que.isempty():
            print(que.get())
        else:
            print("Queue empty")
except:
    print("Queue error!")


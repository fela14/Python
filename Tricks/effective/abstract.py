class Base:
    def foo(self):
        raise NotImplementedError()
    def bar(self):
        raise NotImplementedError()
class Concrete(Base):
    def foo(self):
        return 'foo() called'
    
print(issubclass(Concrete, Base))
b = Base()
# print(b.foo())
c = Concrete()
print(c.foo())
# print(c.bar())

from abc import ABCMeta, abstractmethod

class Base(metaclass = ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass
class Concrete(Base):
    def foo(self):
        return('foo') 
    # def bar(self):
    #     return('bar')

    
print(issubclass(Concrete, Base))
c = Concrete()  # If a class inherits from an abstract base class, 
                # it must implement all abstract methods 
                # before it can be instantiated.



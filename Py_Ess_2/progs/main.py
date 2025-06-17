import module
# __name__ in module.py prints module 
# if (__name__) == "__main__": block prints i like to be a module

# #module.counter()

from module import suml, prodl


zeroes=[0 for x in range(5)]
ones=[1 for x in range(5)]
print(suml(zeroes))
print(prodl(ones))
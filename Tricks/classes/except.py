# def validate(name):
#     if len(name) < 10:
#         raise ValueError
# print(validate('ewa'))

# Defining your own exception

class NameTooShort(ValueError):
    pass
def Validate(name):
    if len(name) < 10:
        raise NameTooShort(name)
try:
    print(Validate('ewa'))
except NameTooShort as e:
    print(e)


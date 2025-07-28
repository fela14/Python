def apply_discount(product, discount):
    amount = int(product['price'] * (1.0 - discount))
    assert 0 <= amount <= product['price']
    return amount

shoes = {'name': 'Fancy shoes', 'price': 14900}
print(apply_discount(shoes, 0.25))
# print(apply_discount(shoes, 1.25))

class AuthError(Exception):
    # Raised when authentication or authorization fails
    pass

class User:
    def __init__(self, username, admin=False):
        self.username = username
        self.admin = admin

    def is_admin(self):
        return self.admin

class Product:
    def __init__(self, prod_id, name):
        self.prod_id = prod_id
        self.name = name

    def delete(self):
        return f'{self.name} with {self.prod_id} has been deleted'

    def __str__(self):
        return f'Product({self.prod_id}, {self.name})'

class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.prod_id] = product

    def has_product(self, prod_id):
        return prod_id in self.products

    def get_product(self, prod_id):
        return self.products.get(prod_id)

    def delete_product(self, prod_id, user):
        assert user.is_admin(), 'Must be an admin'
        assert self.has_product(prod_id), 'Unknown'
        message = self.get_product(prod_id).delete()
        del self.products[prod_id]
        return message

# --- Usage ---
user1 = User('Alice', True)
my_toy = Product(123, "Toy")
my_store = Store()
my_store.add_product(my_toy)

print(my_store.get_product(123))            # Product(123, Toy)
print(my_store.delete_product(123, user1))  # Toy with 123 has been deleted


    # def delete_product(self, prod_id, user):
    #     if not user.is_admin():
    #         raise AuthError('Must be admin to delete')
    #     if not store.has_product(prod_id):
    #         raise ValueError('Unknown product id')
    #     store.get_product(prod_id).delete()
    #     del self.products[prod_id]

store = Store()
product1 = Product(101, 'Toy Car')
store.add_product(product1)
my_product = store.get_product(101)
print(product1.name)
print(product1.prod_id)

user_admin = User('Alice', admin = True)
user_regular = User('Bob', admin = False)
new_user = User('Eve')

# ✅ This works (admin user)
store.delete_product(101, user_admin)

"""
# ❌This will raise an error (not an admin)
store.delete_product(101, user_regular)

# ❌ This will raise an error (product doesn't exist)
store.delete_product(999, user_admin)

# ❌This will raise an error (not an admin)
store.delete_product(101, new_user)
"""

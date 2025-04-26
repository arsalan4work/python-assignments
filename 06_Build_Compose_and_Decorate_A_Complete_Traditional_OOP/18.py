# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value
    
    @price.deleter
    def price(self):
        print(f"Deleting the price of {self.name}")
        del self._price

# Creating a product object
product = Product("Laptop", 20000)
# Accessing price using @property
print(product.price)

# Updating the price using @price.setter
product.price = 30000
print(product.price)

# Tring to set a negative price
product.price = -500

# Deleting the price using @price.deleter
del product.price
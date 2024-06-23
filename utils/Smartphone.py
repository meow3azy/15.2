from .Product import Product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

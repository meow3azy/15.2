from .Product import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

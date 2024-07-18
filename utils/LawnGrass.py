from utils.Product import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, type):
        super().__init__(name, description, price, quantity)
        self.type = type

    def display(self):
        return f"LawnGrass: {self.type} {self.name} - {self.description}: {self.price} ({self.quantity} available)"

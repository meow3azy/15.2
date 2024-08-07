from utils.Product import Product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, brand):
        super().__init__(name, description, price, quantity)
        self.brand = brand

    def display(self):
        return f"Smartphone: {self.brand} {self.name} - {self.description}: {self.price} ({self.quantity} available)"

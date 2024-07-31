from utils.Product import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, grass_type):
        super().__init__(name, description, price, quantity)
        self.grass_type = grass_type
        print(f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.grass_type}') создан")

    def display(self):
        return f"LawnGrass: {self.grass_type} {self.name} - {self.description}: {self.price} ({self.quantity} available)"

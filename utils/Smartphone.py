from utils.Product import Product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, brand):
        super().__init__(name, description, price, quantity)
        self.brand = brand

    def __repr__(self):
        return f"Smartphone(name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity}, brand='{self.brand}')"

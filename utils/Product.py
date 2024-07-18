from utils.abstract_product import AbstractProduct
from utils.mixin import ObjectCreationMixin

class Product(AbstractProduct, ObjectCreationMixin):
    def __init__(self, name, description, price, quantity):
        super().__init__()
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"Product: {self.name} - {self.description}: {self.price} ({self.quantity} available)"

    def apply_discount(self, discount):
        self.price -= self.price * discount

    def increase_price(self, amount):
        self.price += amount

    def calculate_total_value(self):
        return self.price * self.quantity

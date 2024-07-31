from abc import ABC, abstractmethod
from utils.mixin import ObjectCreationMixin

class AbstractProduct(ABC, ObjectCreationMixin):
    @abstractmethod
    def display(self):
        pass

class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        print(f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity}) создан")

    def display(self):
        return f"Product: {self.name} - {self.description}: {self.price} ({self.quantity} available)"

    def apply_discount(self, discount):
        self.price -= self.price * discount

    def increase_price(self, amount):
        self.price += amount

    def calculate_total_value(self):
        return self.price * self.quantity

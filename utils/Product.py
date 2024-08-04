from abc import ABC, abstractmethod
from utils.mixin import ObjectCreationMixin

class AbstractProduct(ABC):
    @abstractmethod
    def display(self):
        pass

class Product(AbstractProduct, ObjectCreationMixin):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"Product: {self.name} - {self.description}: {self.price} ({self.quantity} available)"

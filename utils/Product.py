from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @abstractmethod
    def display_info(self):
        pass


class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Name: {self.name}, Description: {self.description}, Price: {self.price}, Quantity: {self.quantity}")

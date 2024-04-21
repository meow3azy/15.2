from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def display_info(self):
        pass

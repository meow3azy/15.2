from .abstract_product import AbstractProduct

class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.description}, Цена - {self.price} руб, Остаток - {self.quantity} шт"

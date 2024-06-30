from utils.abstract_product import AbstractProduct
from utils.mixin import ObjectCreationMixin
class Product(AbstractProduct, ObjectCreationMixin):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}: {self.description}, Цена - {self.price} руб, Остаток - {self.quantity} шт"

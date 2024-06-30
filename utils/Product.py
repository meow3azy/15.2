from utils.abstract_product import AbstractProduct

class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}: {self.description}, Цена - {self.price} руб, Остаток - {self.quantity} шт"

    def get_total_price(self):
        return self.price * self.quantity

    def reduce_quantity(self, amount):
        if amount > 0 and amount <= self.quantity:
            self.quantity -= amount
            print(f"Количество товара '{self.name}' уменьшено на {amount} шт.")
        else:
            print(f"Невозможно уменьшить количество товара '{self.name}' на указанное количество.")

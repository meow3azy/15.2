from .Product import Product

class Order:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты класса Product")
        self.items.append(product)

    def __str__(self):
        return f"Заказ содержит: {len(self.items)} товаров"

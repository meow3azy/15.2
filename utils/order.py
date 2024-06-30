from utils.Product import Product
from utils.mixin import ObjectCreationMixin


class Order:
    def __init__(self, order_id, products=None):
        self.order_id = order_id
        self.items = []  # Атрибут для хранения продуктов в заказе
        if products is not None:
            self.items.extend(products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты класса Product")
        self.items.append(product)

    def total_price(self):
        return sum(product.price * product.quantity for product in self.products)

    def __str__(self):
        return f"Заказ содержит: {len(self.items)} товаров"

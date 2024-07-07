from .Product import Product

class Order:
    def __init__(self, order_id, products=None):
        self.order_id = order_id
        self.products = products if products is not None else []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты класса Product")
        self.products.append(product)

    def total_price(self):
        return sum(product.calculate_total_value() for product in self.products)

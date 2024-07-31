from utils.Product import Product
from utils.mixin import ObjectCreationMixin

class Order(ObjectCreationMixin):
    def __init__(self, order_id, products):
        super().__init__(order_id, products)
        self.order_id = order_id
        self.products = products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты класса Product")
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)

from .mixin import ObjectCreationMixin

class Category(ObjectCreationMixin):
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."

    def __iter__(self):
        return iter(self.products)
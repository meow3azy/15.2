from utils.mixin import ObjectCreationMixin


class Category(ObjectCreationMixin):
    def __init__(self, name, products=None):
        super().__init__()
        self.name = name
        self.products = products if products is not None else []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display_products(self):
        for product in self.products:
            print(product.display())

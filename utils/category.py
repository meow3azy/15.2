from utils.Product import Product
from utils.mixin import ObjectCreationMixin

class Category:
    class Category(ObjectCreationMixin):
        def __init__(self, name, products):
            self.name = name
            self.products = products
            super().__init__()
    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Товар должен быть экземпляром класса Product")
        self.__products.append(product)

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."

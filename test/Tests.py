import unittest

from LawnGrass import LawnGrass
from Product import Product
from Smartphone import Smartphone
from order import Order


class TestObjects(unittest.TestCase):
    def test_product_creation(self):
        product = Product("Product", "Description of Product", 100, 5)
        self.assertEqual(product.name, "Product1")
        self.assertEqual(product.description, "Description of Product")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.quantity, 5)

    def test_smartphone_creation(self):
        smartphone = Smartphone("Samsung Galaxy", "High-end smartphone", 1000, 10, "Samsung", "Galaxy", "256GB",
                                "Black")
        self.assertEqual(smartphone.name, "Samsung Galaxy")
        self.assertEqual(smartphone.description, "High-end smartphone")
        self.assertEqual(smartphone.price, 1000)
        self.assertEqual(smartphone.quantity, 10)
        self.assertEqual(smartphone.manufacturer, "Samsung")
        self.assertEqual(smartphone.model, "Galaxy")
        self.assertEqual(smartphone.storage_capacity, "256GB")
        self.assertEqual(smartphone.color, "Black")

    def test_lawn_grass_creation(self):
        lawn_grass = LawnGrass("Grass", "Green Grass", 50, 100, "USA", "2 weeks", "Green")
        self.assertEqual(lawn_grass.name, "Grass")
        self.assertEqual(lawn_grass.description, "Green Grass")
        self.assertEqual(lawn_grass.price, 50)
        self.assertEqual(lawn_grass.quantity, 100)
        self.assertEqual(lawn_grass.country_of_origin, "USA")
        self.assertEqual(lawn_grass.germination_period, "2 weeks")
        self.assertEqual(lawn_grass.color, "Green")

    def test_order_creation(self):
        product = Product("Product", "Description of Product", 100, 5)
        order = Order(product, 2, 200)
        self.assertEqual(order.product, product)
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.total_cost, 200)


if __name__ == "__main__":
    unittest.main()

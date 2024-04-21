from LawnGrass import LawnGrass
from Product import Product
from Smartphone import Smartphone
from order import Order


def main():
    # Создание продуктов
    product1 = Product("Product", "Description of Product1", 100, 5)
    smartphone = Smartphone("Samsung Galaxy", "High-end smartphone", 1000, 10, "Samsung", "Galaxy", "256GB", "Black")
    lawn_grass = LawnGrass("Grass", "Green Grass", 50, 100, "USA", "2 weeks", "Green")

    # Создание заказа
    order = Order(product1, 2, 200)

    # Вывод информации о созданных объектах
    print(product1.__dict__)
    print(smartphone.__dict__)
    print(lawn_grass.__dict__)
    print(order.__dict__)


if __name__ == "__main__":
    main()

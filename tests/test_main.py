import pytest
from utils.Product import Product
from utils.Smartphone import Smartphone
from utils.order import Order
from utils.category import Category


@pytest.fixture
def create_smartphone():
    return Smartphone("Smartphone", "High-end smartphone", 1000, 50, "Brand X")


@pytest.fixture
def create_order():
    return Order(order_id=123)


def test_order_creation(create_order):
    order = create_order
    assert order.order_id == 123
    assert order.products == []


def test_product_initialization():
    product = Product("Product1", "Description of Product1", 500, 20)
    assert product.name == "Product1"
    assert product.description == "Description of Product1"
    assert product.price == 500
    assert product.quantity == 20


def test_add_product_to_order(create_order, create_smartphone):
    order = create_order
    product = create_smartphone
    order.add_product(product)
    assert len(order.products) == 1
    assert order.products[0] == product


def test_invalid_product_addition(create_order):
    order = create_order
    with pytest.raises(ValueError):
        order.add_product("Not a Product")


def test_smartphone_creation(create_smartphone):
    smartphone = create_smartphone
    assert smartphone.name == "Smartphone"
    assert smartphone.description == "High-end smartphone"
    assert smartphone.price == 1000
    assert smartphone.quantity == 50
    assert smartphone.brand == "Brand X"

import pytest
from utils.Product import Product
from utils.Smartphone import Smartphone
from utils.LawnGrass import LawnGrass
from utils.order import Order

@pytest.fixture
def create_smartphone():
    return Smartphone("Smartphone", "High-end smartphone", 1000, 50)

@pytest.fixture
def create_lawngrass():
    return LawnGrass("Grass", "Green grass for lawns", 20, 200)

@pytest.fixture
def create_order():
    return Order()

def test_product_initialization(create_smartphone):
    product = create_smartphone
    assert product.name == "Smartphone"
    assert product.description == "High-end smartphone"
    assert product.price == 1000
    assert product.quantity == 50

def test_add_product_to_order(create_order, create_smartphone):
    order = create_order
    product = create_smartphone
    order.add_product(product)
    assert len(order.items) == 1
    assert "Smartphone" in str(order.items[0])

def test_invalid_product_addition(create_order):
    order = create_order
    with pytest.raises(ValueError):
        order.add_product("Не продукт")

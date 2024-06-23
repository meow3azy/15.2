from utils.Smartphone import Smartphone
from utils.LawnGrass import LawnGrass
from utils.order import Order

smartphone = Smartphone("Smartphone", "High-end smartphone", 1000, 50)
grass = LawnGrass("Grass", "Green grass for lawns", 20, 200)

order = Order()
order.add_product(smartphone)
order.add_product(grass)

print(order)

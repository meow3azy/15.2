from abc import ABC, abstractmethod


class AbstractOrder(ABC):
    @abstractmethod
    def __init__(self, product, quantity, total_cost):
        pass


class Order(AbstractOrder):
    def __init__(self, product, quantity, total_cost):
        self.product = product
        self.quantity = quantity
        self.total_cost = total_cost

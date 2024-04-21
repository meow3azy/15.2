from abc import ABC, abstractmethod


class AbstractOrder(ABC):
    def __init__(self, product, quantity, total_cost):
        self.product = product
        self.quantity = quantity
        self.total_cost = total_cost

    @abstractmethod
    def display_order(self):
        pass

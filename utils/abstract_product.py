from abc import ABC, abstractmethod


from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def display(self):
        pass


    @abstractmethod
    def apply_discount(self, discount):
        pass

    @abstractmethod
    def increase_price(self, amount):
        pass

    @abstractmethod
    def calculate_total_value(self):
        pass

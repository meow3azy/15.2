from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    @abstractmethod
    def display_info(self):
        pass

class ObjectCreationLoggerMixin:
    def __repr__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"
from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass

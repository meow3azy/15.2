from main import AbstractProduct, ObjectCreationLoggerMixin


class Smartphone(AbstractProduct):
    def __init__(self, name, price, manufacturer, model, storage_capacity, color):
        super().__init__(name, price, "Smartphone")
        self.manufacturer = manufacturer
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def display_info(self):
        print(f'Смартфон: {self.name}, Производитель: {self.manufacturer}, Модель: {self.model}, Цена: {self.price}')


class Smartphone(ObjectCreationLoggerMixin):
    def __init__(self, name, manufacturer, model, storage_capacity, color):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

from main import AbstractProduct


class Smartphone(AbstractProduct):
    def __init__(self, name, description, price, quantity, manufacturer, model, storage_capacity, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def display_info(self):
        super().display_info()
        print(
            f"Manufacturer: {self.manufacturer}, Model: {self.model}, Storage Capacity: {self.storage_capacity}, Color: {self.color}")

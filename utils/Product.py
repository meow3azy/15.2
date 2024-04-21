from main import AbstractProduct


class Product(AbstractProduct):
    def display_info(self):
        print(f"Name: {self.name}, Description: {self.description}, Price: {self.price}, Quantity: {self.quantity}")

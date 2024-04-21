from abstractorder import AbstractOrder


class Order(AbstractOrder):
    def display_order(self):
        print(f"Product: {self.product}, Quantity: {self.quantity}, Total Cost: {self.total_cost}")

from main import AbstractProduct


class LawnGrass(AbstractProduct):
    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def display_info(self):
        super().display_info()
        print(
            f"Country of Origin: {self.country_of_origin}, Germination Period: {self.germination_period}, Color: {self.color}")

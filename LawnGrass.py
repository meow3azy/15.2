from main import AbstractProduct, ObjectCreationLoggerMixin

class LawnGrass(AbstractProduct):
    def __init__(self, name, price, country_of_origin, germination_period, color):
        super().__init__(name, price, "Lawn Grass")
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return f"Газон: {self.name}, Страна происхождения: {self.country_of_origin}, Период прорастания: {self.germination_period}, Цена: {self.price}"
class LawnGrass(ObjectCreationLoggerMixin):
    def __init__(self, name, country_of_origin, germination_period, color):
        self.name = name
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

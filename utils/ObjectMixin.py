class ObjectCreationLoggerMixin:
    def __init__(self, name, description, price, quantity, **kwargs):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.kwargs = kwargs

    def __repr__(self):
        attributes = ", ".join([f"{key}={value}" for key, value in self.kwargs.items()])
        return f"{self.__class__.__name__}({attributes})"

    def create_object(self):
        print(f"Object created: {self}")

class ObjectCreationMixin:
    def __init__(self):
        print(f"Создан объект {self.__class__.__name__} с атрибутами: {self.__dict__}")

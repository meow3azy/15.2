class ObjectCreationMixin:
    def __init__(self, *args):
        print(f"{self.__class__.__name__} создан с атрибутами: {args}")

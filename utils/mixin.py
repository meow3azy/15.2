class ObjectCreationMixin:
    def __init__(self):
        super().__init__()
        print(f"{self.__class__.__name__} создан с атрибутами: {self.__dict__}")

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items())})"

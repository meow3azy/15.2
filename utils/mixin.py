class ObjectCreationMixin:
    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__} создан с атрибутами: {', '.join(f'{k}={v}' for k, v in kwargs.items())}")


    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items())})"

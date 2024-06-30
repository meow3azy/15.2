class ObjectCreationMixin:
    def __repr__(self):
        attr_list = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attr_list})"

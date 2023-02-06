from types import MappingProxyType


class OpenApiRegister:
    __service__ = set()

    def __init__(self, prefix, name, *args, **kwargs):
        self.api_name = f"{prefix}.{name}"

    def __call__(self, func):
        self.__service__.add(self.api_name)

        return func


class OpenApiFactory(OpenApiRegister):

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass


@OpenApiRegister(prefix="test", name="api.register")
def test_func(a, b):
    return a + b


@OpenApiRegister(prefix="test", name="api.register_c")
def test_func_c(a, b):
    return a + b


print(OpenApiRegister.__service__)
print(OpenApiFactory.__service__)
print(test_func(10, 5))

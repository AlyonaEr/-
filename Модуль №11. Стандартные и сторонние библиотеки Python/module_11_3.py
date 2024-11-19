import inspect


class Pets:
    def __init__(self, name):
        self.name = name


def introspection_info(obj):
    return (f'type: {type(obj)}\n'
            f'attributes: {getattr(obj, 'name')}\n'
            f'methods: {dir(obj)}\n'
            f'module: {inspect.getmodule(obj)}')


pets_1 = Pets("Alisa")
number_info = introspection_info(pets_1)
print(number_info)

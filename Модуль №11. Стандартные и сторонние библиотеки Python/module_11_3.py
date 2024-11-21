import inspect


class Pets:
    def __init__(self, name):
        self.name = name


def introspection_info(obj):
    return (f'type: {type(obj)}\n'
            f'attributes: {getattr(obj, 'name', 'атрибут отсутствует')}\n'
            f'methods: {dir(obj)}\n'
            f'module: {inspect.getmodule(obj)}')


pets_1 = Pets("Alisa")
list_1 = ['Sea', 12, ('red', 'blue', 1)]
string_1 = 'i am a string'
number_info_1 = introspection_info(pets_1)
print(number_info_1)
number_info_2 = introspection_info(24)
print(number_info_2)
number_info_3 = introspection_info(list_1)
print(number_info_3)
number_info_4 = introspection_info(string_1)
print(number_info_4)
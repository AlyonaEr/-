# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(12, False)
print_params('проверка')
print_params('True', 12, False)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
values_list = [14, False, 'распаковка']
values_dict = {'a': 25.5, 'b': True, 'c': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [17, [2, 3]]
print_params(*values_list_2, 42)

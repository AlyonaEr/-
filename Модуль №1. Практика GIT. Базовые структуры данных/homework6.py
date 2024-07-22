my_dict = {'Nikita': 1998, 'Olya': 2001, 'Vera': 1975}
print(my_dict)
print(my_dict['Nikita'])
print(my_dict.get('Anna', 'Такого ключа нет'))
my_dict.update({'Katya': 2011, 'Vlad': 1980})
n = my_dict.pop('Vera')
print(n)
print(my_dict)
my_set = {1, 15, 24, 'Blue', True, 15, 1, 'Blue'}
print(my_set)
my_set.add((10, 28, 34))
my_set.add('Red')
my_set.discard(1)
print(my_set)

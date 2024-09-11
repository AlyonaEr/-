from pprint import pprint

file_name = 'text.txt'


def custom_write(file_name, strings):
    strings_positions = {}
    for i, j in enumerate(strings):
        file = open(file_name, 'a', encoding='utf-8')
        t = file.tell()
        file.write(str(j) + "\n")
        strings_positions[(i + 1, t)] = j
        file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
     print(elem)

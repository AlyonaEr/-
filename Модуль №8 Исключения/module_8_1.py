def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError as exc:
        print(f'вот что пошло не так - {exc}, но мы ещё на плаву')
        print(f'{a}{b}')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

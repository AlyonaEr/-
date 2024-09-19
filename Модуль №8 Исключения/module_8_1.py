def add_everything_up(a, b):
    try:
        print (a + b)
    except TypeError as exc:
        print(f'вот что пошло не так - {exc}, но мы ещё на плаву')
        print(f'{a}{b}')

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)

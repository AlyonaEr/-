def is_prime(func):
    def wrapper(*args):
        sum_three_result = func(*args)
        if sum_three_result % 2 != 0:
            print(f'Простое')
        if sum_three_result % 2 == 0:
            print(f'Составное')
        return sum_three_result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

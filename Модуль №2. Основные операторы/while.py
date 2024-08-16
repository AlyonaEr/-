import random

n = random.randint(3, 20)
result = ''
i = 1
while i < n:
    i += 1
    j = i + 1
    while j < n:
        j += 1
        if n % (i + j) == 0:
            result += f"{i}{j}"
print(n, result)

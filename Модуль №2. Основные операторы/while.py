import random

n = random.randint(3, 20)
result = ''
i = 0
while i < n:
    i += 1
    j = i
    while j < n:
        j += 1
        if n % (i + j) == 0:
            result += f"{i}{j}"
print(n, result)

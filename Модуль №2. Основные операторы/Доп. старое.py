import random

n = random.randint(3,20)
result = ''
while 1>0:
if i in range(1,n):
    if j in range (i+1, n):
        if n % (i+j) == 0:
            result+=f"{i}{j}"
print(n, result)
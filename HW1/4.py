# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

from random import random, randint
from string import ascii_lowercase

inp = input('dimension: ').split()
dim_min, dim_max = min(inp), max(inp)

result = ''
if dim_min in ascii_lowercase and dim_max in ascii_lowercase:
    result = chr(randint(ord(dim_min), ord(dim_max)))
elif dim_min.isdigit() and dim_max.isdigit():
    result = randint(int(dim_min), int(dim_max))
else:
    result = (float(dim_max) - float(dim_min)) * random() + float(dim_min)

print(result)

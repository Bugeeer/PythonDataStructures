# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.

from string import ascii_uppercase, digits
from collections import ChainMap, deque
from itertools import zip_longest
from timeit import timeit
from functools import partial, reduce
from statistics import median

base = 16
assert 1 < base < len(digits+ascii_uppercase) + 1

# generate correspondence table
digits_dict = {char: index for index, char in enumerate(digits)}
digits_dict_inverted = {index: char for index, char in enumerate(digits)}
letters_dict = {char: index + 10 for index, char in enumerate(ascii_uppercase[:base - 10])}
letters_dict_inverted = {index + 10: char for index, char in enumerate(ascii_uppercase[:base - 10])}

number = ChainMap(digits_dict, letters_dict, digits_dict_inverted, letters_dict_inverted)


def addition_v1(a: str, b: str) -> str:
    """ Addition of two numbers: preferred """
    result = ''
    next_cap_add = 0
    for an, bn in zip_longest(reversed(a), reversed(b), fillvalue='0'):
        s = number[an] + number[bn] + next_cap_add
        next_cap_add = s // base
        n = s % base
        result += number[n]
    return f'{number[next_cap_add] if next_cap_add else ""}{result[::-1]}'


def addition_v2(a: str, b: str) -> str:
    """ Addition of two numbers: another way """
    a, b = deque(a), deque(b)
    result = ''
    next_cap_add = 0
    for _ in max(a.copy(), b.copy(), key=deque.__len__):
        an = a.pop() if len(a) > 0 else '0'
        bn = b.pop() if len(b) > 0 else '0'
        s = number[an] + number[bn] + next_cap_add
        next_cap_add = s // base
        n = s % base
        result += number[n]
    return f'{number[next_cap_add] if next_cap_add else ""}{result[::-1]}'


def multiple(a: str, b: str) -> str:
    """ Multiple of two numbers """
    result = []

    for d_cap, an in enumerate(reversed(a)):
        next_cap_add, sub = 0, ''
        for bn in reversed(b):
            s = number[an] * number[bn] + next_cap_add
            next_cap_add = s // base
            n = s % base
            sub += number[n]
        result.append(f'{number[next_cap_add] if next_cap_add else ""}{sub[::-1]}{"0" * d_cap}')

    return reduce(addition_v1, result)


def analysis(a, b, loop=20000):
    f1 = partial(addition_v1, a, b)
    f2 = partial(addition_v2, a, b)
    f3 = partial(multiple, a, b)
    print(f'Run-time analysis:')
    print(f'add v1: median = {median([timeit(f1, number=1) for _ in range(loop)])}')
    print(f'add v2: median = {median([timeit(f2, number=1) for _ in range(loop)])}')
    print(f'mul v2: median = {median([timeit(f3, number=1) for _ in range(loop)])}')


# input numbers
n1, n2 = input(f'Enter two nums (base={base}): ').upper().split()
# n1, n2 = 'F9', '134'  # + -> 22D    * -> 12B94

print(f'{n1} + {n2} = {addition_v1(n1, n2)}')
print(f'{n1} * {n2} = {multiple(n1, n2)}')

# analysis(n1, n2)

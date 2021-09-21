# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# я перепробовал кучу алгоритмов из прошлых уроков, но все они ели памяти +/- одинаково: см. результат
# по задаче 4 из урока 3.
# В задаче с Эратосфеном отличия мне показались более наглядными, поэтому взял её

from itertools import count
from math import sqrt, log
import sys
from memory_profiler import profile
import tracemalloc


@profile
def algorithm_1(target):
    primes = [2]
    rng = int(1.5 * target * log(target))
    for number in range(3, rng, 2):
        for prime in primes:    # check whether the current number is divisible by all prime numbers before it
            if number % prime == 0:
                break       # divisor found
        else:
            primes.append(number)
            if len(primes) >= target:
                break
    return f'The {target}-th prime number is {primes[-1]}'


@profile
def algorithm_2(target):     # iterating through divisors
    primes = [2]
    for number in count(3):
        for divisor in range(2, number):
            if number % divisor == 0:       # divisor found => number is not prime
                break
        else:
            primes.append(number)
            if len(primes) == target:        # break if target number was found
                break
    return f'The {target}-th prime number is {primes[-1]}'


@profile
def algorithm_3(target):
    primes = [3]
    for number in count(3, 2):     # start from 3, cause 2 is already known as prime number
        # check whether the current number is divisible by prime numbers < sqrt(number)
        sq_num = sqrt(number)
        is_prime = False
        for prime in primes:
            if prime > sq_num:
                is_prime = True
                break       # нет смысла искать дальше
            if number % prime == 0:
                break       # divisor found
        if is_prime:
            primes.append(number)
            if len(primes) >= target:
                break
    primes = [2, *primes]
    return f'The {target}-th prime number is {primes[-1]}'


@profile
def algorithm_3_lim(target):
    primes = [3]
    rng = int(1.5 * target * log(target))
    for number in range(3, rng, 2):     # start from 3, cause 2 is already known as prime number
        # check whether the current number is divisible by prime numbers < sqrt(number)
        sq_num = sqrt(number)
        is_prime = False
        for prime in primes:
            if prime > sq_num:
                is_prime = True
                break       # нет смысла искать дальше
            if number % prime == 0:
                break       # divisor found
        if is_prime:
            primes.append(number)
            if len(primes) >= target:
                break
    primes = [2, *primes]
    return f'The {target}-th prime number is {primes[-1]}'


# Задание 4 из урока 3 - Определить, какое число в массиве встречается чаще всего.
# v1
@profile
def additional_1(source):
    max_counter = 1
    number = 0
    for index in range(len(source) - 1):
        counter = 1
        for compare_index in range(index + 1, len(source)):
            counter += bool(source[index] == source[compare_index])
        if max_counter < counter:
            max_counter = counter
            number = source[index]
    print(f'Number {number} occurs {max_counter} times in the sequence')


# v2
@profile
def additional_2(source):
    max_counter = 1
    number = 0
    counter = {}
    for num in source:
        if counter.get(num):
            counter[num] += 1
        else:
            counter.update({num: 1})

    for num, cnt in counter.items():
        if max_counter < cnt:
            max_counter = cnt
            number = num
    print(f'Number {number} occurs {max_counter} times in the sequence')


# просто ради интереса: задание 7 урока 3
@profile
def les_3_t_7(source: list):
    first_min, second_min = source[0], source[0]
    for index in range(len(source)):
        if source[index] <= first_min:
            second_min = first_min
            first_min = source[index]
            continue
        if source[index] < second_min:
            second_min = source[index]
    print(f'Two smallest values: {first_min}, {second_min}')


if __name__ == '__main__':
    def analyse(title, func, *args):
        print('-' * 25, title, '-' * 25)
        tracemalloc.clear_traces()
        print(func(*args))
        mem_current, mem_peak = tracemalloc.get_traced_memory()
        print(f'{title}> current: {mem_current}, peak {mem_peak}')


    data = [10, 15, 41, 3, -80, -13, 17, 8, 3, -6, 1, 11, 15, -7, -3, -19, 10, 7, 93, 11, 7, 14, 22, 7]
    n = 500

    print(sys.version, sys.platform)
    tracemalloc.start()
    analyse('ALGORITHM 1', algorithm_1, n)
    analyse('ALGORITHM 2', algorithm_2, n)
    analyse('ALGORITHM 3', algorithm_3, n)
    analyse('ALGORITHM 3 LIM', algorithm_3_lim, n)

    analyse('ADD1', additional_1, data)
    analyse('ADD2', additional_2, data)
    analyse('L3T7', les_3_t_7, data)
    tracemalloc.stop()

# Выводы по memory_profiler:
# Windows 64 bit, Python 3.9
# 0) под все объекты скрипта выделено примерно 20 МиБ
# 1) При малых значениях target все алгоритмы равноценны, при увеличении target начинает чудить алгоритм 2
# 2) при высоких значениях target алгоритм 3 занимает памяти как будто бы чуть меньше и освобождает её раньше
# 3) алгоритмы первых трех уроков неинтересно рассматривать с точки зрения использования памяти
#       в виду отсутствия динамики. Но из вариантов задания 4 урока 3 предпочтительнее вариант 1 (алгоритм additional_1)
#       ибо он есть меньше памяти на максимуме
# ------------------------- ALGORITHM 1 -------------------------
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     15     20.7 MiB     20.7 MiB           1   @profile
#     16                                         def algorithm_1(target):
#     17     20.7 MiB      0.0 MiB           1       primes = [2]
#     18     20.7 MiB      0.0 MiB           1       rng = int(1.5 * target * log(target))
#     19     20.7 MiB      0.0 MiB        1785       for number in range(3, rng, 2):
#     20     20.7 MiB      0.0 MiB      130261           for prime in primes:    # check whether the current number is divisible by all prime numbers before it
#     21     20.7 MiB      0.0 MiB      129762               if number % prime == 0:
#     22     20.7 MiB      0.0 MiB        1286                   break       # divisor found
#     23                                                 else:
#     24     20.7 MiB      0.0 MiB         499               primes.append(number)
#     25     20.7 MiB      0.0 MiB         499               if len(primes) >= target:
#     26     20.7 MiB      0.0 MiB           1                   break
#     27     20.7 MiB      0.0 MiB           1       return f'The {target}-th prime number is {primes[-1]}'
#
#
# The 500-th prime number is 3571
# ALG1 MEMORY> current: 181306, Peak 249243
# ------------------------- ALGORITHM 2 -------------------------
# Filename: E:\Python projects\Algorithms\lesson_6\task_1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     30     20.5 MiB     20.5 MiB           1   @profile
#     31                                         def algorithm_2(target):     # iterating through divisors
#     32     20.5 MiB      0.0 MiB           1       primes = [2]
#     33     20.6 MiB     -0.6 MiB        3569       for number in count(3):
#     34     20.6 MiB   -210.2 MiB      835324           for divisor in range(2, number):
#     35     20.6 MiB   -210.1 MiB      834825               if number % divisor == 0:       # divisor found => number is not prime
#     36     20.6 MiB     -0.5 MiB        3070                   break
#     37                                                 else:
#     38     20.6 MiB     -0.1 MiB         499               primes.append(number)
#     39     20.6 MiB     -0.1 MiB         499               if len(primes) == target:        # break if target number was found
#     40     20.6 MiB      0.0 MiB           1                   break
#     41     20.6 MiB      0.0 MiB           1       return f'The {target}-th prime number is {primes[-1]}'
#
#
# The 500-th prime number is 3571
# ALG2 MEMORY> current: 856, Peak 20643
# ------------------------- ALGORITHM 3 -------------------------
# Filename: E:\Python projects\Algorithms\lesson_6\task_1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     44     20.6 MiB     20.6 MiB           1   @profile
#     45                                         def algorithm_3(target):
#     46     20.6 MiB      0.0 MiB           1       primes = [3]
#     47     20.6 MiB      0.0 MiB        1785       for number in count(3, 2):     # start from 3, cause 2 is already known as prime number
#     48                                                 # check whether the current number is divisible by prime numbers < sqrt(number)
#     49     20.6 MiB      0.0 MiB        1785           sq_num = sqrt(number)
#     50     20.6 MiB      0.0 MiB        1785           is_prime = False
#     51     20.6 MiB      0.0 MiB       10786           for prime in primes:
#     52     20.6 MiB      0.1 MiB       10786               if prime > sq_num:
#     53     20.6 MiB      0.0 MiB         499                   is_prime = True
#     54     20.6 MiB      0.0 MiB         499                   break       # нет смысла искать дальше
#     55     20.6 MiB      0.0 MiB       10287               if number % prime == 0:
#     56     20.6 MiB      0.0 MiB        1286                   break       # divisor found
#     57     20.6 MiB      0.0 MiB        1785           if is_prime:
#     58     20.6 MiB      0.0 MiB         499               primes.append(number)
#     59     20.6 MiB      0.0 MiB         499               if len(primes) >= target:
#     60     20.6 MiB      0.0 MiB           1                   break
#     61     20.6 MiB      0.0 MiB           1       primes = [2, *primes]
#     62     20.6 MiB      0.0 MiB           1       return f'The {target}-th prime number is {primes[-1]}'
#
#
# The 500-th prime number is 3571
# ALG3 MEMORY> current: 1184, Peak 23736
# ------------------------- ALGORITHM 3 LIM -------------------------
# Filename: E:\Python projects\Algorithms\lesson_6\task_1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     65     20.6 MiB     20.6 MiB           1   @profile
#     66                                         def algorithm_3_lim(target):
#     67     20.6 MiB      0.0 MiB           1       primes = [3]
#     68     20.6 MiB      0.0 MiB           1       rng = int(1.5 * target * log(target))
#     69     20.6 MiB      0.0 MiB        1785       for number in range(3, rng, 2):     # start from 3, cause 2 is already known as prime number
#     70                                                 # check whether the current number is divisible by prime numbers < sqrt(number)
#     71     20.6 MiB      0.0 MiB        1785           sq_num = sqrt(number)
#     72     20.6 MiB      0.0 MiB        1785           is_prime = False
#     73     20.6 MiB      0.0 MiB       10786           for prime in primes:
#     74     20.6 MiB      0.0 MiB       10786               if prime > sq_num:
#     75     20.6 MiB      0.0 MiB         499                   is_prime = True
#     76     20.6 MiB      0.0 MiB         499                   break       # нет смысла искать дальше
#     77     20.6 MiB      0.0 MiB       10287               if number % prime == 0:
#     78     20.6 MiB      0.0 MiB        1286                   break       # divisor found
#     79     20.6 MiB      0.0 MiB        1785           if is_prime:
#     80     20.6 MiB      0.0 MiB         499               primes.append(number)
#     81     20.6 MiB      0.0 MiB         499               if len(primes) >= target:
#     82     20.6 MiB      0.0 MiB           1                   break
#     83     20.6 MiB      0.0 MiB           1       primes = [2, *primes]
#     84     20.6 MiB      0.0 MiB           1       return f'The {target}-th prime number is {primes[-1]}'
#
#
# The 500-th prime number is 3571
# ALG3 LIM MEMORY> current: 928, Peak 23556

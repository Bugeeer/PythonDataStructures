# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена». Второй — без использования «Решета Эратосфена».

# Алгоритмы:
# в 1-ом перебор всех простых делителей до первого успешного деления; сложность O(N) ?
# во 2-ом перебор вообще всех делителей до первого успешного деления; сложность O(N^2)
# в 3-ем перебор всех простых делителей меньше корня из number, до первого успешного деления; сложность тоже O(N)?

# если интересно, приложил график скорости работы алгоритмов (сек) в зависимости от дальности искомого числа:
# для i от 1000 до 19000 с шагом 1000

from itertools import count
from math import sqrt
from task_1 import test_algorithm
import cProfile
from timeit import timeit

target = 1000000


def algorithm_1():
    primes = [2]

    for number in count(3):     # start from 3, cause 2 is already known as prime number
        for prime in primes:    # check whether the current number is divisible by all prime numbers before it
            if number % prime == 0:
                break       # divisor found
        else:
            primes.append(number)
            if len(primes) >= target:
                break
    return f'The {target}-th prime number is {primes[-1]}'


def algorithm_2():     # iterating through divisors
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


def algorithm_3():
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


def algorithm_3_old():
    primes = [2]

    for number in count(3):     # start from 3, cause 2 is already known as prime number
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
    return f'The {target}-th prime number is {primes[-1]}'


if __name__ == '__main__':
    # print(algorithm_1())
    # print(algorithm_2())
    print(algorithm_3())
    # test_algorithm(algorithm_1, algorithm_2, algorithm_3, loops=5)
    test_algorithm(algorithm_3_old, algorithm_3, loops=5)

    # print('----- Algorithm 1 -----')
    # cProfile.run('algorithm_1()')
    # print('----- Algorithm 2 -----')
    # cProfile.run('algorithm_2()')
    print('----- Algorithm 3 Old -----')
    cProfile.run('algorithm_3_old()')
    print('----- Algorithm 3 -----')
    cProfile.run('algorithm_3()')

    # lp = 5
    # for trg in range(1, 20):
    #     target = trg * 1000
    #     print(timeit(algorithm_1, number=lp) / lp)

# OUTPUT:
# The 15000-th prime number is 163841
# Algorithm 1, loops = 10:
#     minimal time: 4.4706667000000095
#     maximal time: 4.826662400000004
#     average time: 4.597649979999998
#     median time: 4.572034399999993
# ------
# Algorithm 2, loops = 10:
#     minimal time: 55.0066061
#     maximal time: 62.9543779
#     average time: 59.30017627999999
#     median time: 60.79520400000001
# ------
# Algorithm 3, loops = 10:
#     minimal time: 0.13377830000001723
#     maximal time: 0.1450428999999076
#     average time: 0.13856887999999118
#     median time: 0.13834385000001248
# ------
# The best algorithm is 3 with avg. time 0.13856887999999118
#    It is 33.17952761110785 times faster than algorithm 1
#    It is 427.94728715425686 times faster than algorithm 2
# ----- Algorithm 1 -----
#          30002 function calls in 5.040 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.040    5.040 <string>:1(<module>)
#         1    5.035    5.035    5.040    5.040 task_2.py:19(algorithm_1)
#         1    0.000    0.000    5.040    5.040 {built-in method builtins.exec}
#     14999    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#     14999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ----- Algorithm 2 -----
#          30002 function calls in 61.376 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   61.376   61.376 <string>:1(<module>)
#         1   61.364   61.364   61.376   61.376 task_2.py:33(algorithm_2)
#         1    0.000    0.000   61.376   61.376 {built-in method builtins.exec}
#     14999    0.005    0.000    0.005    0.000 {built-in method builtins.len}
#     14999    0.007    0.000    0.007    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ----- Algorithm 3 -----
#          193841 function calls in 0.168 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.168    0.168 <string>:1(<module>)
#         1    0.139    0.139    0.168    0.168 task_2.py:47(algorithm_3)
#         1    0.000    0.000    0.168    0.168 {built-in method builtins.exec}
#     14999    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#    163839    0.026    0.000    0.026    0.000 {built-in method math.sqrt}
#     14999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Дополнение по вариантам алгоритма 3:
# The 1000000-th prime number is 15485863
# Algorithm 1, loops = 5:
#     minimal time: 57.32546309999998
#     maximal time: 64.09637230000001
#     average time: 59.64487260000001
#     median time: 58.459247300000015
# ------
# Algorithm 2, loops = 5:
#     minimal time: 57.00206159999999
#     maximal time: 65.06095400000004
#     average time: 59.33923560000001
#     median time: 57.76897889999998
# ------
# The best algorithm is 2 with avg. time 59.33923560000001
#    It is 1.0051506730228252 times faster than algorithm 1
# ----- Algorithm 3 Old -----
#          17485863 function calls in 61.463 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.010    0.010   61.462   61.462 <string>:1(<module>)
#         1   58.606   58.606   61.452   61.452 task_2.py:71(algorithm_3_old)
#         1    0.000    0.000   61.463   61.463 {built-in method builtins.exec}
#    999999    0.113    0.000    0.113    0.000 {built-in method builtins.len}
#  15485861    2.581    0.000    2.581    0.000 {built-in method math.sqrt}
#    999999    0.152    0.000    0.152    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ----- Algorithm 3 -----
#          9742933 function calls in 60.276 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.012    0.012   60.276   60.276 <string>:1(<module>)
#         1   58.642   58.642   60.264   60.264 task_2.py:50(algorithm_3)
#         1    0.000    0.000   60.276   60.276 {built-in method builtins.exec}
#    999999    0.120    0.000    0.120    0.000 {built-in method builtins.len}
#   7742931    1.351    0.000    1.351    0.000 {built-in method math.sqrt}
#    999999    0.152    0.000    0.152    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# любопытно, что при очень больших искомых значениях, разница во времени нивелируется

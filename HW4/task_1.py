# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.

# Для анализа взял решения задания 4 из урока 3:
# Определить, какое число в массиве встречается чаще всего. Сложность: линейная O(n)

from random import randint
from timeit import timeit
from statistics import mean, median

source = [randint(-20, 20) for _ in range(1000)]


def algorithm_1():
    max_counter = 1
    number = 0
    for index in range(len(source) - 1):
        counter = 1
        for compare_index in range(index + 1, len(source)):
            counter += bool(source[index] == source[compare_index])
        if max_counter < counter:
            max_counter = counter
            number = source[index]
    return number, max_counter


def algorithm_2():
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

    return number, max_counter


def algorithm_3():
    import functools as ft

    a = source
    e, c = ft.reduce((lambda l, n: l if l[1] >= n[1] else n), [(n, len([1 for e in a if e == n])) for n in set(a)],
                     (-1, -1))
    return e, c


def test_algorithm(*args, **kwargs):
    loops = kwargs.get('loops', 1000)

    times = {}
    for number, arg in enumerate(args, start=1):
        times[number] = [timeit(arg, number=1) for _ in range(loops)]

    mean_times = {alg: mean(time) for alg, time in times.items()}
    median_times = {alg: median(time) for alg, time in times.items()}
    best_alg = min(mean_times, key=mean_times.get)

    for alg, time in times.items():
        print(f'Algorithm {alg}, loops = {loops}:')
        print(f'    minimal time: {min(time)}')
        print(f'    maximal time: {max(time)}')
        print(f'    average time: {mean_times.get(alg)}')
        print(f'    median time: {median_times.get(alg)}')
        print('------')

    print(f'The best algorithm is {best_alg} with avg. time {mean_times.get(best_alg)}')
    compare = [f'   It is {time / mean_times.get(best_alg)} times faster than algorithm {alg}'
               for alg, time in mean_times.items() if alg != best_alg]
    print(*compare, sep='\n')


if __name__ == '__main__':
    test_algorithm(algorithm_1, algorithm_2, algorithm_3, loops=100)

# OUTPUT:
# Algorithm 1, loops = 100:
#     minimal time: 0.06359330000000085
#     maximal time: 0.16620360000000023
#     average time: 0.08264894200000006
#     median time: 0.07756300000000005
# ------
# Algorithm 2, loops = 100:
#     minimal time: 0.00011099999999863996
#     maximal time: 0.0002651000000000181
#     average time: 0.00012376700000011454
#     median time: 0.00011740000000060036
# ------
# Algorithm 3, loops = 100:
#     minimal time: 0.0008859999999994983
#     maximal time: 0.003084100000000589
#     average time: 0.0009940290000000117
#     median time: 0.0009595000000004461
# ------
# The best algorithm is 2 with avg. time 0.00012376700000011454
#    It is 667.7785031545046 times faster than algorithm 1
#    It is 8.031454264861326 times faster than algorithm 3

# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.

from analyzer import print_analyze, values
from random import choice
from statistics import median


# @print_analyze
def heap_sort(data, reverse=False):
    """ Heap sorting """

    def heap_sift(_data, _root, _size=None):
        if not _size:
            _size = len(_data)
        root_index = _root
        left_index = 2 * root_index + 1  # left child index
        right_index = 2 * root_index + 2  # right child index

        if left_index < _size and _data[left_index] > _data[root_index]:
            root_index = left_index
        if right_index < _size and _data[right_index] > _data[root_index]:
            root_index = right_index

        if root_index != _root:
            _data[root_index], _data[_root] = _data[_root], _data[root_index]
            heap_sift(_data, root_index, _size)

    length = len(data)
    # build primary tree
    for index in range(length, -1, -1):
        heap_sift(data, index)
    # move head to the end of list and rebuild tree without moved values
    for index in range(length - 1):
        data[0], data[-1 - index] = data[-1 - index], data[0]
        heap_sift(data, 0, length - 1 - index)

    if reverse:
        for index in range(len(data) // 2):
            data[index], data[-1 - index] = data[-1 - index], data[index]


@print_analyze
def classic_median(data):
    heap_sort(data)
    ld = len(data)
    if ld % 2 == 1:
        return data[ld // 2]
    else:
        i = ld // 2
        return sum(data[i - 1:i + 1]) / 2


@print_analyze
def find_median(data: list):
    """ Based on Hoare's algorithm but without sorting
        google it: "hoare's selection" or "quickselect" """
    def get_element(_data: list, position=None):
        if len(_data) == 1:
            return _data[0]

        pivot = choice(_data)       # generate pivot

        lesser = [elem for elem in _data if elem < pivot]
        greater = [elem for elem in _data if elem > pivot]
        pivots = [elem for elem in _data if elem == pivot]

        if position < len(lesser):
            # recursively find in lesser
            return get_element(lesser, position)
        elif position < len(lesser) + len(pivots):
            return pivot
        else:
            # recursively find in greater
            position -= len(lesser) + len(pivots)
            return get_element(greater, position)

    length = len(data)
    pos = length // 2
    if length % 2 == 1:
        return get_element(data, pos)
    else:
        return (get_element(data, pos - 1) + get_element(data, pos)) / 2


if __name__ == '__main__':
    source = values((-10., 10), count=101, dig_round=2)
    print(f'Source:     | length={len(source)}\n{source}')
    print(find_median(source))
    print(classic_median(source))
    print(f'[MEDIAN CHECK] {median(source)}')

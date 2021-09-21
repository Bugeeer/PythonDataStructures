# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from analyzer import print_analyze, values


@print_analyze
def merge_sort(data, reverse=False):
    """ Merge sorting """
    def merge(_left: list, _right: list):
        result = []
        li, ri = 0, 0

        while li < len(_left) and ri < len(_right):
            if ((_left[li] < _right[ri]) ^ reverse) and _left[li] != _right[ri]:
                result.append(_left[li])
                li += 1
            else:
                result.append(_right[ri])
                ri += 1

        result.extend(_left[li:])
        result.extend(_right[ri:])
        return result

    mid = len(data) // 2
    if mid == 0:
        return data[:]
    else:
        left = merge_sort(data[:mid], reverse)
        right = merge_sort(data[mid:], reverse)
        return merge(left, right)


if __name__ == '__main__':
    source = values((.0, 50), count=100)
    print(f'Source:     | length={len(source)}\n{source}')
    print(merge_sort(source, reverse=True))

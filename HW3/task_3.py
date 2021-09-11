# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

source = [19, 3, 7, 4, 9, 12, 35, 22, 76, 13, 88, 514]

min_elem, max_elem = source[0], source[0]
for elem in source:
    # get min and max values without min() & max() methods
    min_elem = elem if elem < min_elem else min_elem
    max_elem = elem if elem > max_elem else max_elem

min_index, max_index = source.index(min_elem), source.index(max_elem)
source[min_index], source[max_index] = max_elem, min_elem
print(source)

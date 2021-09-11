# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

source = [10, 15, 41, 3, -80, -13, 17, 8, 3, -6, 1, 11, 15, -7, -3, -19, 10, 7, 93, 11, 7, 14, 22, 7]

min_elem, max_elem = source[0], source[0]
min_index, max_index = 0, 0
for index in range(len(source)):
    # get min and max values without min() & max() methods
    if source[index] < min_elem:
        min_elem = source[index]
        min_index = index
    if source[index] > max_elem:
        max_elem = source[index]
        max_index = index

start_index, stop_index = (min_index, max_index) if min_index < max_index else (max_index, min_index)
sum_source = 0
for index in range(start_index + 1, stop_index):
    sum_source += source[index]

print(sum_source)

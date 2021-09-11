# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
# собой (оба минимальны), так и различаться.

source = [10, 15, 41, 3, -80, -13, 17, 8, 3, -6, 1, 11, 15, -7, -3, -19, 10, 7, 93, 11, 7, 14, 22, 7]

first_min, second_min = source[0], source[0]
min_index, max_index = 0, 0

for index in range(len(source)):
    if source[index] <= first_min:
        second_min = first_min
        first_min = source[index]
        continue
    if source[index] < second_min:
        second_min = source[index]

print(f'Two smallest values: {first_min}, {second_min}')

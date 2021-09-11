# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[3, 4, 5, 12],
          [1, 2, 4, 7],
          [1, 7, 6, 14],
          [9, 3, 1, 13],
          [0, 4, 5, 9]]

t_matrix = list(zip(*matrix))


min_elements = []
for row in t_matrix:
    minimal = row[0]
    for element in row:
        if element < minimal:       # find min element in each row
            minimal = element
    min_elements.append(minimal)

max_element = min_elements[0]
for element in min_elements:        # find max of minimals
    if element > max_element:
        max_element = element

print(f'Max of row minimals = {max_element}')

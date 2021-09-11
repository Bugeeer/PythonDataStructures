# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

source = [2, -20, -13, 17, 8, 3, -6, 1, 11, 15, -7, -3, -19]
negatives = [num for num in source if num < 0]
result = negatives[0]
result_index = 0

for num in negatives:
    if abs(num) < abs(result):
        result = num
        result_index = source.index(num)

print(f'Max negative = {result}, index = {result_index}')

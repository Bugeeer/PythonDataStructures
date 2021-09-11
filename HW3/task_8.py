# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []
for row in range(5):
    nums = list(map(int, input(f'Enter 3 nums for row {row}: ').split()))

    num_sum = 0
    for num in nums:
        num_sum += num
    nums.append(num_sum)
    matrix.append(nums)

print(matrix)

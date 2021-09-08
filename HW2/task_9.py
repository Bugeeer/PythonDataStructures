# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

nums = input('Enter numbers: ').split()
max_sum = 0
n = None
for num in nums:
    s = sum(list(map(int, num)))
    if s > max_sum:
        max_sum = s
        n = num

print(f'Number: {n}, sum = {max_sum}')
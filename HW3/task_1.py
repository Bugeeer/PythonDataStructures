# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

result = []
for num in range(2, 100):
    for divisor in range(2, 10):
        counter = int(not bool(num % divisor))      # аналогично: counter = 1 if num % divisor == 0 else 0
        try:
            result[divisor - 2] += counter
        except IndexError:
            result.append(counter)

print('In range [2, 99]:')
for num in range(2, 10):
    print(f'multiple of {num}: {result[num - 2]}')

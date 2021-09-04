# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

n1, n2, n3 = map(int, input('Enter 3 numbers: ').split())

result = ''
if n2 < n1 < n3 or n3 < n1 < n2:
    result = n1
elif n1 < n2 < n3 or n3 < n2 < n1:
    result = n2
else:
    result = n3
print('Average num:', result)

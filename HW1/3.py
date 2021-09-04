# По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.


x1, y1 = map(float, input('Enter coordinate 1: ').split())
x2, y2 = map(float, input('Enter coordinate 2: ').split())

# print(x1, y1, x2, y2)

k = (y1 - y2) / (x1 - x2)
b = (x1 * y2 - x2 * y1) / (x1 - x2)

print(f'Function: y = {k}x {"+" if b >= 0 else "-"} {abs(b)}')

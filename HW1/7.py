# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.


a, b, c = map(float, input('Enter 3 numbers: ').split())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Triangle is equilateral.')
    elif a == b or a == c or c == b:
        print('Triangle is isosceles.')
    else:
        print("Just triangle.")
else:
    print("Triangle not exists.")

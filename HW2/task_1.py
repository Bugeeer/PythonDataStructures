# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.Числа и знак операции вводятся
# пользователем.После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.\
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
# неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

operation = ''
while operation != '0':
    operation = input('operation: ')

    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        if operation != '0':
            print('Incorrect operation. Try again.')
        continue

    n1, n2 = map(float, input('Enter 2 numbers: ').split())

    result = 0
    try:
        exec(f'result = {n1} {operation} {n2}')
    except ZeroDivisionError:
        print('Division by zero is undefined.')
        continue

    print(f'Result = {result}')

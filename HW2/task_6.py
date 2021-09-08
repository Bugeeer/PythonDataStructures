# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем
# за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

import random

number = random.randint(0, 100)
max_counts = 10
count = 0

is_winner = False
while not is_winner:
    count += 1
    num = int(input(f'({count}) Guess a num: '))

    if num == number:
        print('You win.')
        is_winner = True
        break

    if count >= max_counts:
        print(f'You loose. My number was {number}')
        break
    elif number < num:
        print('My number is lower.')
    else:
        print('My number is higher.')

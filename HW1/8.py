# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = input('Enter year: ')

year = int(year)
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print('Not leap year')
else:
    print('Leap year')

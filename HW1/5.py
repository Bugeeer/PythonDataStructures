# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

from string import ascii_lowercase

char_1, char_2 = input('Enter two chars: ').split()

pos_1 = ascii_lowercase.find(char_1.lower()) + 1
pos_2 = ascii_lowercase.find(char_2.lower()) + 1


print(f'Char "{char_1}" position: {pos_1}')
print(f'Char "{char_2}" position: {pos_2}')
print(f'Interval: {abs(pos_2 - pos_1) - 1} chars')

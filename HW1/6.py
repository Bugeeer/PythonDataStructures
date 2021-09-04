# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

pos = int(input('Enter char number: '))
char = chr(ord('a') + pos - 1)
print(f'Char "{char}"')

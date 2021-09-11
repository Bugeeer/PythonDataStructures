# Определить, какое число в массиве встречается чаще всего.

source = [10, 15, 22, 41, 3, 14, 10, 13, 22, 7, 7, 7, 41, 19, 10, 7, 93, 11, 7, 14, 22, 7]

max_counter = 1
number = 0

# v1
for index in range(len(source) - 1):
    counter = 1
    for compare_index in range(index + 1, len(source)):
        counter += bool(source[index] == source[compare_index])
    if max_counter < counter:
        max_counter = counter
        number = source[index]
print(f'Number {number} occurs {max_counter} times in the sequence')

# v2
counter = {}
for num in source:
    if counter.get(num):
        counter[num] += 1
    else:
        counter.update({num: 1})

for num, cnt in counter.items():
    if max_counter < cnt:
        max_counter = cnt
        number = num

print(f'Number {number} occurs {max_counter} times in the sequence')

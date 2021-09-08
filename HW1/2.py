# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

n1, n2 = 5, 6

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2

print(f"SOURCE: {bin(n1)}, {bin(n2)}")
print(f" OR: {bin(bit_or)}")
print(f"AND: {bin(bit_and)}")
print(f"XOR: {bin(bit_xor)}")

shr = n1 >> 2
shl = n1 << 2

print(f"SHR: {bin(shr)}")
print(f"SHL: {bin(shl)}")

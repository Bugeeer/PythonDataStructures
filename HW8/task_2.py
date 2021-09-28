# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from collections import deque, Counter, defaultdict
from operator import itemgetter
from math import log2


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # def get_code(self, data):
    #     if self.data == data:
    #         return ' '
    #     res = self.left.get_code(data) if self.left else None
    #     if res:
    #         return '0' + res
    #     res = self.right.get_code(data) if self.right else None
    #     if res:
    #         return '1' + res
    #     return ''


class Tree:
    def __init__(self, root: Node = None, source: str = ''):
        self.root = root
        if not self.root and source:
            self.build(source)

    def build(self, source: str):
        """ Построение бинарного дерева """
        counter = Counter(source)       # определяем частоты вхождения символов
        deq = deque()
        for char, freq in sorted(counter.items(), key=itemgetter(1)):   # добавляем в очередь
            deq.append(Node(char))

        while len(deq) > 1:
            left = deq.popleft()
            right = deq.popleft()

            priority = 0        # считаем приоритет нового узла
            priority += counter[left.data] if counter[left.data] else left.data
            priority += counter[right.data] if counter[right.data] else right.data
            new_node = Node(priority, left, right)

            # ищем место для вставки нового узла в очередь
            p_index = len(deq)
            for index, node in enumerate(deq):
                pr = counter[node.data] if counter[node.data] else node.data
                if priority <= pr:
                    p_index = index
                    break
            deq.insert(p_index, new_node)

        self.root = deq.pop()

    def encode_symbol(self, data):
        # return self.root.get_code(data)       # это тоже вариант, но с рекурсией
        deq = deque([self.root])
        num = 0
        passes = set()
        while len(deq) > 0:
            node = deq.pop()
            num += 1

            corrected = False
            while not corrected:        # корректируем num
                corrected = True
                for pn in passes:
                    if float.is_integer(log2(num / pn)):
                        num += 2 ** (int(log2(num)) - int(log2(pn)))
                        corrected = False

            # или вот простой способ:
            # for pn in passes.copy():       # корректируем num
            #     if num % pn == 0:
            #         passes.update([num, num + 1])
            #         passes.remove(pn)
            #         num += 2

            if node.data == data:
                break

            if node.left:
                deq.appendleft(node.left)
            if node.right:
                deq.appendleft(node.right)
            if not node.left and not node.right:
                passes.add(num)
        else:
            num = 0
        z = bin(num)
        a = bin(num)[3:]
        b = bin(num)[2:]
        return bin(num)[3:]

    def encode(self, source):
        table = defaultdict(str, {key: self.encode_symbol(key) for key in set(source)})
        result = ''
        for sym in source:
            result += table[sym]
        return result

    def decode(self, source):
        s = source[:]
        node = self.root
        result = ''
        for index in range(len(s)):
            prev_node = node
            node = node.right if int(source[index]) else node.left
            if not node:
                result += prev_node.data
                node = self.root.right if int(source[index]) else self.root.left
        if isinstance(node.data, str):
            result += node.data
        return result


if __name__ == '__main__':
    src = 'beep boop beer!'
    # src = 'Warriors of the World!'

    tree = Tree(source=src)
    # print('b', tree.encode_symbol('b'), tree.decode(tree.encode_symbol('b')))
    # print(' ', tree.encode_symbol(' '), tree.decode(tree.encode_symbol(' ')))
    # print('o', tree.encode_symbol('o'), tree.decode(tree.encode_symbol('o')))
    # print('r', tree.encode_symbol('r'), tree.decode(tree.encode_symbol('r')))
    # print('!', tree.encode_symbol('!'), tree.decode(tree.encode_symbol('!')))
    # print('p', tree.encode_symbol('p'), tree.decode(tree.encode_symbol('p')))
    # print('e', tree.encode_symbol('e'), tree.decode(tree.encode_symbol('e')))
    # print('-' * 50)
    # print(tree.encode_symbol('G'))

    print(tree.encode(src))
    print(tree.encode('r'))
    print(tree.decode('0011111010100001101110101000111110001001'))
    print(tree.decode('00100001111110001100111011010110001111010100010111010101001100111110111100011001'))


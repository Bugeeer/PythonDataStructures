# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, 
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib


def hash_find_all(source: str, sub: str) -> list:
    if (not len(source) and not len(sub)) or len(source) < len(sub):
        return []

    len_sub = len(sub)
    hash_sub_sha256 = hashlib.sha256(sub.encode('utf-8')).hexdigest()
    hash_sub_md5 = hashlib.md5(sub.encode('utf-8')).hexdigest()

    result = []
    index = 0
    while index < len(source) - len_sub + 1:
        hash_sha256 = hashlib.sha256(source[index:index + len_sub].encode('utf-8')).hexdigest()
        hash_md5 = hashlib.md5(source[index:index + len_sub].encode('utf-8')).hexdigest()
        # проверка по двум хешам просто так. ну и приятный бонус: минимизация шанса коллизии
        if hash_sub_sha256 == hash_sha256 and hash_sub_md5 == hash_md5:
            result.append(index)        # добавляем индекс вхождения
            index += len_sub            # проскакиваем вперед на длину подстроки - сомнительная операция, но пускай
        index += 1

    return result


if __name__ == '__main__':
    s1, s2 = 'stroka rok okurok ukurok', 'rok'
    index_list = hash_find_all(s1, s2)
    print(f"Source: '{s1}' | sub: '{s2}'\nItems found: {len(index_list)}\nStart indexes:", *index_list)

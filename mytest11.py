HASH1 = 17
HASH2 = 223


class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.bit_array = [0] * self.filter_len

    def hash1(self, str1):
        # 17
        hash_value = 0
        for c in str1:
            code = ord(c)
            hash_value = (hash_value * HASH1 + code) % self.filter_len
        return hash_value
        # реализация ...

    def hash2(self, str1):
        hash_value = 0
        for c in str1:
            code = ord(c)
            hash_value = (hash_value * HASH2 + code) % self.filter_len

        return hash_value

    def add(self, str1):
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        self.bit_array[index1] = 1
        self.bit_array[index2] = 1

    # добавляем строку str1 в фильтр

    def is_value(self, str1):
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)
        return self.bit_array[index1] == 1 and self.bit_array[index2] == 1

# проверка, имеется ли строка str1 в фильтре

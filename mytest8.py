class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        total = 0
        for i in range(len(value)):
            total += ord(value[i]) * (7 ** i)
        return (len(value) * total) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        while index < self.size:
            if self.slots[index] is None or self.slots[index] == value:
                return index
            index += self.step
        return None

    def put(self, value):
        index_to_put = self.seek_slot(value)
        if index_to_put is None:
            return None
        self.slots[index_to_put] = value
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        return index_to_put

    def find(self, value):
        index = self.seek_slot(value)
        if index is None:
            return None
        if self.slots[index] != value:
            return None
        return index

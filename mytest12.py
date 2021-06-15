class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        min_hits_value = self.hits[0]
        min_hits_index = 0
        while index < self.size:
            if self.slots[index] is None or self.slots[index] == value:
                return index
            if min_hits_value < self.hits[index]:
                min_hits_value = self.hits[index]
                min_hits_index = index
            index += 3

        return min_hits_index

    def hash_fun(self, value):
        total = 0
        for i in range(len(value)):
            total += ord(value[i]) * (7 ** i)
        return (len(value) * total) % self.size

    def is_key(self, key):
        for slot in self.slots:
            if slot == key:
                return True
        return False

    def put(self, key, value):
        index = self.seek_slot(key)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        if not self.is_key(key):
            return None
        index = self.seek_slot(key)
        self.hits[index] += 1
        return self.values[index]

class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, value):
        total = 0
        for i in range(len(value)):
            total += ord(value[i]) * (7 ** i)
        return (len(value) * total) % self.size

    def is_key(self, key):
        index = self.hash_fun(key)
        return self.slots[index] is not None

    def put(self, key, value):
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        if not self.is_key(key):
            return None
        return self.values[self.hash_fun(key)]

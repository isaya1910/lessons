# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        self.dict = {}

    def size(self):
        return len(self.dict.keys())
        # количество элементов в множестве

    def print(self):
        print(*self.dict.keys())

    def put(self, value):
        self.dict[value] = value

    def get(self, value):
        return self.dict.get(value) is not None

    def remove(self, value):
        # возвращает True если value удалено
        if self.get(value):
            self.dict.pop(value)
            return True
        return False

    def intersection(self, set2):
        ans = PowerSet()
        for key in self.dict.keys():
            if set2.get(key):
                ans.put(key)
        return ans

    def union(self, set2):
        ans = PowerSet()
        for key in self.dict.keys():
            ans.put(key)

        for key in set2.dict.keys():
            ans.put(key)
        return ans

    def difference(self, set2):
        # разница текущего множества и set2
        ans = PowerSet()
        for key in self.dict.keys():
            if not set2.get(key):
                ans.put(key)
        return ans

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for key in set2.dict.keys():
            if not self.get(key):
                return False
        return True

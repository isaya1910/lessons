import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.count = self.count + 1
        for j in range(self.count - 1, i, -1):
            self.array[j] = self.array[j - 1]
        self.array[i] = itm

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.count = self.count - 1
        if self.capacity / self.count > 2:
            new_capacity = int((self.capacity * 2) / 3)
            if new_capacity >= 16:
                self.capacity = new_capacity


def insert_test():
    dynArray = DynArray()
    for i in range(40):
        dynArray.append(11)
    print(*dynArray)

    dynArray.insert(5, 14)

    print(*dynArray)


def delete_test():
    dynArray = DynArray()
    dynArray.append(23)
    dynArray.append(24)

    for i in range(100):
        dynArray.append(11)
    print(*dynArray)

    for i in range(0, 100):
        dynArray.delete(1)

    print(*dynArray)

import ctypes


class DynArray:

    # array --> capacity_array
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.capacity_array = self.make_array(self.capacity)

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
        self.capacity_array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.capacity_array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.count = self.count + 1
        for j in range(self.count - 1, i, -1):
            self.capacity_array[j] = self.capacity_array[j - 1]
        self.capacity_array[i] = itm

    # percent--> capacity_percent
    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        for j in range(i, self.count - 1):
            self.capacity_array[j] = self.capacity[j + 1]
        self.count = self.count - 1
        capacity_percent = self.count / self.capacity
        if capacity_percent < 0.5:
            new_capacity = int((self.capacity * 2) / 3)
            if new_capacity >= 16:
                self.capacity = new_capacity
            else:
                self.capacity = 16

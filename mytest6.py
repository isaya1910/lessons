class Deque:
    def __init__(self):
        self.list = []

    def addFront(self, item):
        self.list.insert(0, item)

    def addTail(self, item):
        self.list.append(item)

    def removeFront(self):
        if len(self.list) == 0:
            return None
        return self.list.pop(0)

    def removeTail(self):
        if len(self.list) == 0:
            return None

        return self.list.pop()  # если очередь пуста

    def size(self):
        return len(self.list)  # размер очереди

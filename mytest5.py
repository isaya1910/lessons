class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, item: int):
        self.list.append(item)

    def dequeue(self):
        if len(self.list) == 0:
            return None
        return self.list.pop(0)

    def size(self):
        return len(self.list)

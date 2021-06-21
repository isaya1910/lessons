class Stack:
    # stack --> items
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def pop(self):
        # ваш код
        if len(self.items) > 0:
            return self.items.pop()
        return None  # если стек пустой

    def push(self, value):
        self.items.append(value)

    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        return None

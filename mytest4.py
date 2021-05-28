class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        # ваш код
        if len(self.stack) > 0:
            return self.stack.pop()
        return None  # если стек пустой

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return None

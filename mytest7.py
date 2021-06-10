class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.size = 0

    def compare(self, v1, v2):
        if v1 < v2: return -1
        if v1 > v2: return 1
        return 0

    def __add_tail(self, node):
        temp = self.tail
        self.tail = node
        node.prev = temp
        temp.next = node

    def __add_head(self, node):
        temp = self.head
        self.head = node
        node.next = temp
        temp.prev = node

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        elif self.head is not None and self.tail is None:
            if self.compare(node.value, self.head.value) == 1 or self.compare(node.value, self.head.value) == 0:
                if self.__ascending:
                    node.prev = self.head
                    self.head.next = node
                    self.tail = node
                else:
                    temp = self.head
                    node.next = temp
                    temp.prev = node
                    self.head = node
                    self.tail = temp
            else:
                if self.__ascending:
                    temp = self.head
                    node.next = temp
                    temp.prev = node
                    self.head = node
                    self.tail = temp
                else:
                    node.prev = self.head
                    self.head.next = node
                    self.tail = node
        elif self.head is not None and self.tail is not None:
            if self.__ascending:
                it = self.tail
                while it is not None and (self.compare(it.value, node.value) == 1 or self.compare(it.value,
                                                                                                  node.value) == 0):
                    it = it.prev
                if it is None:
                    self.__add_head(node)
                elif it is self.tail:
                    self.__add_tail(node)
                else:
                    temp = it
                    node.prev = temp
                    node.next = temp.next
                    temp.next.prev = node
                    temp.next = node

            else:
                it = self.head
                while it is not None and (
                        self.compare(it.value, node.value) == 1 or self.compare(it.value, node.value) == 0):
                    it = it.next
                if it is None:
                    self.__add_tail(node)
                elif it is self.head:
                    self.__add_head(node)
                else:
                    temp = it
                    node.next = temp
                    node.prev = temp.prev
                    temp.prev.next = node
                    temp.prev = node
        self.size += 1

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def update_tail(self):
        node = self.head
        self.tail = self.head
        while node is not None:
            self.tail = node
            node = node.next

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                prev = node.prev
                next = node.next
                if prev is not None:
                    prev.next = next
                    if next is not None:
                        next.prev = prev
                else:
                    self.head = next
                    if next is not None:
                        next.prev = None
                self.size -= 1
                break
            node = node.next
        self.update_tail()

    def clean(self, asc):

        self.__ascending = asc
        self.head = None
        self.tail = None
        self.size = 0

    def len(self):
        return self.size  # здесь будет ваш код

    def get_all(self):

        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        trim_string1 = v1.rstrip()
        trim_string1 = trim_string1.lstrip()

        trim_string2 = v2.rstrip()
        trim_string2 = trim_string2.lstrip()

        if trim_string1 > trim_string2:
            return 1
        if trim_string1 < trim_string2:
            return -1
        return 0

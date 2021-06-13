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

    def add(self, value):
        if self.__ascending:
            self.asc_ordered_list(value)
        else:
            self.desc_ordered_list(value)

    def asc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        if self.head.next is None:
            if self.compare(self.head.value, data) == 1:
                temp = self.head
                self.head = new_node
                self.tail = temp
                new_node.next = temp
                temp.prev = new_node
            else:
                self.head.next = new_node
                new_node.prev = self.head
                self.tail = new_node
            return
        temp = self.head
        while temp is not None:
            if self.compare(temp.value, data) == 1:
                break
            temp = temp.next
        if temp is None:
            old_tail = self.tail
            old_tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node
            return

        tt = temp.prev
        temp.prev = new_node
        new_node.prev = tt
        if tt is not None:
            tt.next = new_node
        else:
            self.head = new_node
        new_node.next = temp

    def desc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        if self.head.next is None:
            if self.compare(self.head.value, data) == -1:
                temp = self.head
                self.head = new_node
                self.tail = temp
                new_node.next = temp
                temp.prev = new_node
            else:
                self.head.next = new_node
                new_node.prev = self.head
                self.tail = new_node
            return
        temp = self.head
        while temp is not None:
            if self.compare(temp.value, data) == -1:
                break
            temp = temp.next
        if temp is None:
            old_tail = self.tail
            old_tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node
            return

        tt = temp.prev
        temp.prev = new_node
        new_node.prev = tt
        if tt is not None:
            tt.next = new_node
        else:
            self.head = new_node
        new_node.next = temp

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        temp = self.head

        if temp is not None:
            if temp.value == val:
                self.head = temp.next
                temp.prev = None
                return
        while temp is not None:
            if temp.value == val:
                break
            temp = temp.next
        if temp is None:
            return
        temp.prev.next = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp is self.tail:
            self.tail = self.tail.prev
            if self.tail == self.head:
                self.tail = None

    def clean(self, asc):

        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        ans = 0
        while node is not None:
            ans += 1
            node = node.next
        return ans

    def get_all(self):

        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def get_all_values(self):

        r = []
        node = self.head
        while node is not None:
            r.append(node.value)
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

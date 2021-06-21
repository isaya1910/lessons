class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    # __ascending --> __is_ascending
    def __init__(self, __is_ascending):
        self.head = None
        self.tail = None
        self.__is_ascending = __is_ascending
        self.size = 0

    def compare(self, v1, v2):
        if v1 < v2: return -1
        if v1 > v2: return 1
        return 0

    def add(self, value):
        if self.__is_ascending:
            self.asc_ordered_list(value)
        else:
            self.desc_ordered_list(value)

    def asc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        if self.head.next is None:
            # temp --> old_head
            if self.compare(self.head.value, data) == 1:
                old_head = self.head
                self.head = new_node
                self.tail = old_head
                new_node.next = old_head
                old_head.prev = new_node
            else:
                self.head.next = new_node
                new_node.prev = self.head
                self.tail = new_node
            return
        # temp --> node_iteration
        node_iteration = self.head
        while node_iteration is not None:
            if self.compare(node_iteration.value, data) == 1:
                break
            node_iteration = node_iteration.next
        if node_iteration is None:
            old_tail = self.tail
            old_tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node
            return

        # tt --< previous_node
        previous_node = node_iteration.prev
        node_iteration.prev = new_node
        new_node.prev = previous_node
        if previous_node is not None:
            previous_node.next = new_node
        else:
            self.head = new_node
        new_node.next = node_iteration

    def desc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        if self.head.next is None:
            if self.compare(self.head.value, data) == -1:
                # temp --> old_head
                old_head = self.head
                self.head = new_node
                self.tail = old_head
                new_node.next = old_head
                old_head.prev = new_node
            else:
                self.head.next = new_node
                new_node.prev = self.head
                self.tail = new_node
            return
        # temp --> node_iteration
        node_iteration = self.head
        while node_iteration is not None:
            if self.compare(node_iteration.value, data) == -1:
                break
            node_iteration = node_iteration.next
        if node_iteration is None:
            old_tail = self.tail
            old_tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node
            return
        # tt --< previous_node
        previous_node = node_iteration.prev
        node_iteration.prev = new_node
        new_node.prev = previous_node
        if previous_node is not None:
            previous_node.next = new_node
        else:
            self.head = new_node
        new_node.next = node_iteration

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

    # prev --> previous_node
    # next --> next_node
    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                previous_node = node.prev
                next_node = node.next
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.prev = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.prev = None
                self.update_tail()
                return
            node = node.next

    def clean(self, asc):

        self.__is_ascending = asc
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

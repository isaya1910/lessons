class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedListParent:
    def __init__(self):
        self._dummy_head = Node(None)
        self._dummy_tail = Node(None)

        self._dummy_head.next = self._dummy_tail
        self._dummy_tail.prev = self._dummy_head


class LinkedList2(LinkedListParent):
    def __init__(self):
        super().__init__()
        self.length = 0

    def get_head(self):
        return self._dummy_head.next

    def get_tail(self):
        return self._dummy_tail.prev

    def add_in_tail(self, item):
        old_tail = self.get_tail()
        old_tail.next = item
        item.prev = old_tail
        self._dummy_tail.prev = item
        item.next = self._dummy_tail
        self.length = self.length + 1

    def find(self, val):
        node = self._dummy_head.next
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self._dummy_head.next
        ans = []
        while node is not None:
            if node.value == val:
                ans.append(node)
            node = node.next
        return ans

    def delete(self, val, all=False):
        node = self._dummy_head.next
        while node is not None:
            if node.value == val:
                prev = node.prev
                next = node.next
                prev.next = next
                next.prev = prev
                self.length = self.length - 1
                if not all:
                    return
            node = node.next

    def clean(self):
        self._dummy_head.next = self._dummy_tail
        self._dummy_tail.prev = self._dummy_head

    def len(self):
        return self.length

    def insert(self, afterNode, new_node):
        if afterNode is None:
            if self.len() == 0:
                self.add_in_head(new_node)
            else:
                self.add_in_tail(new_node)
        else:
            node = self._dummy_head.next
            while node is not None:
                if node is afterNode:
                    buff = node.next
                    node.next = new_node
                    new_node.prev = node
                    buff.prev = new_node
                    new_node.next = buff
                node = node.next
        self.length = self.length + 1

    def add_in_head(self, new_node):
        old_head = self.get_head()
        self._dummy_head.next = new_node
        new_node.next = old_head
        old_head.prev = new_node
        self.length = self.length + 1

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

    # item --> new_node
    def add_in_tail(self, new_node):
        old_tail = self.get_tail()
        old_tail.next = new_node
        new_node.prev = old_tail
        self._dummy_tail.prev = new_node
        new_node.next = self._dummy_tail
        self.length = self.length + 1

    def find(self, val):
        node = self._dummy_head.next
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # ans --> nodes val-->node_value_to_delete
    def find_all(self, nodes_value_to_find):
        node = self._dummy_head.next
        nodes = []
        while node is not None:
            if node.value == nodes_value_to_find:
                nodes.append(node)
            node = node.next
        return nodes

    # val --> node_value_to_delete
    def delete(self, node_value_to_delete, all=False):
        node = self._dummy_head.next
        while node is not None:
            if node.value == node_value_to_delete:
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                self.length = self.length - 1
                if not all:
                    return
            node = node.next

    def clean(self):
        self._dummy_head.next = self._dummy_tail
        self._dummy_tail.prev = self._dummy_head

    def len(self):
        return self.length

    def insert(self, after_node, new_node):
        if after_node is None:
            if self.len() == 0:
                self.add_in_head(new_node)
            else:
                self.add_in_tail(new_node)
            self.length = self.length + 1

        else:
            node = self._dummy_head.next
            while node is not None:
                if node is after_node:
                    buff = node.next
                    node.next = new_node
                    new_node.prev = node
                    buff.prev = new_node
                    new_node.next = buff
                    self.length = self.length + 1
                node = node.next

    def add_in_head(self, new_node):
        old_head = self.get_head()
        self._dummy_head.next = new_node
        new_node.next = old_head
        old_head.prev = new_node
        self.length = self.length + 1

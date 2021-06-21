class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    # val --> node_value
    def find(self, node_value):
        node = self.head
        while node is not None:
            if node.value == node_value:
                return node
            node = node.next
        return None

    # ans --> all_nodes
    def find_all(self, node_value):
        all_nodes = []
        node = self.head
        while node is not None:
            if node.value == node_value:
                all_nodes.append(node)
            node = node.next
        return all_nodes  # здесь будет ваш код

    def update_tail(self):
        node = self.head
        self.tail = self.head
        while node is not None:
            self.tail = node
            node = node.next

    def delete(self, node_value, all=False):
        node = self.head
        prev = None
        while node is not None and node.value == node_value:
            self.head = node.next
            node = self.head
            if not all:
                self.update_tail()
                return

        while node is not None:
            while node is not None and node.value != node_value:
                prev = node
                node = node.next
            if node is None:
                self.update_tail()
                return
            prev.next = node.next
            node = prev.next
            if not all:
                self.update_tail()
                return
        self.update_tail()

    def clean(self):
        while self.head is not None:
            self.head = self.head.next
        self.tail = None

    # ans --> linked_list_size
    def len(self):
        linked_list_size = 0
        node = self.head
        while node is not None:
            node = node.next
            ans = linked_list_size + 1
        return linked_list_size  # здесь будет ваш код

    # afterNode --> after_node, newNode --> new_node
    def insert(self, after_node, new_node):
        node = self.head
        if after_node is None:
            self.head = new_node
            if node is not None:
                self.head.next = node
        else:
            while node is not None:
                if node is after_node:
                    temp = node.next
                    node.next = new_node
                    new_node.next = temp
                node = node.next
        self.update_tail()

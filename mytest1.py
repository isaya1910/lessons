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

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        ans = []
        node = self.head
        while node is not None:
            if node.value == val:
                ans.append(node)
            node = node.next
        return ans  # здесь будет ваш код

    def update_tail(self):
        node = self.head
        self.tail = self.head
        while node is not None:
            self.tail = node
            node = node.next

    def delete(self, val, all=False):
        node = self.head
        prev = None
        while node is not None and node.value == val:
            self.head = node.next
            node = self.head
            if not all:
                self.update_tail()
                return

        while node is not None:
            while node is not None and node.value != val:
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

    def clean(self):
        while self.head is not None:
            self.head = self.head.next
        self.tail = None

    def len(self):
        ans = 0
        node = self.head
        while node is not None:
            node = node.next
            ans = ans + 1
        return ans  # здесь будет ваш код

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode is None:
            self.head = newNode
            if node is not None:
                self.head.next = node
        else:
            while node is not None:
                if node is afterNode:
                    temp = node.next
                    node.next = newNode
                    newNode.next = temp
                node = node.next


def delete_test():
    linked_list = LinkedList()

    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(7))
    linked_list.add_in_tail(Node(5))

    linked_list.print_all_nodes()
    linked_list.delete(5, False)
    linked_list.print_all_nodes()
   # assert linked_list.head is None

    #assert linked_list.tail is None

def clean_test():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(5))
    linked_list.clean()
    linked_list.clean()
    assert linked_list.len() == 0
    assert linked_list.head is None
    assert linked_list.tail is None


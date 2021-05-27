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
        self.update_tail()

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
        self.update_tail()


def delete_test():
    linked_list = LinkedList()

    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(5))
    linked_list.delete(5, True)
    assert linked_list.len() == 0
    assert linked_list.head is None
    assert linked_list.tail is None

    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(6))
    linked_list.add_in_tail(Node(6))

    linked_list.delete(6, False)
    assert linked_list.tail.value == 6
    linked_list.add_in_tail(Node(6))
    linked_list.delete(6, True)
    assert linked_list.tail.value == 5


delete_test()


def clean_test():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(6))
    linked_list.clean()
    assert linked_list.len() == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def find_all_test():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(6))
    list = linked_list.find_all(6)
    assert len(list) == 1
    assert list[0].value == 6


def len_test():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(6))
    assert linked_list.len() == 2


def insert_test():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(6))
    linked_list.insert(None, Node(7))
    assert linked_list.head.value == 7

    linked_list.insert(linked_list.head, Node(5))
    node = linked_list.find(5)
    assert node is not None
    assert linked_list.head.next is node


insert_test()


def task1_8(linked_list_1: LinkedList, linked_list_2: LinkedList):
    ans = []
    if linked_list_1.len() == linked_list_2.len():
        node1 = linked_list_1.head
        node2 = linked_list_2.head
        while node1 is not None and node2 is not None:
            ans.append(node1.value + node2.value)
            node1 = node1.next
            node2 = node2.next
        return ans


def task1_8_test():
    linked_list1 = LinkedList()
    linked_list1.add_in_tail(Node(6))
    linked_list1.add_in_tail(Node(7))
    linked_list1.add_in_tail(Node(7))

    linked_list2 = LinkedList()
    linked_list2.add_in_tail(Node(6))
    linked_list2.add_in_tail(Node(7))
    linked_list2.add_in_tail(Node(7))

    ans = task1_8(linked_list1, linked_list2)
    assert ans[0] == 12
    linked_list1.add_in_tail(Node(5))
    ans = task1_8(linked_list1, linked_list2)
    assert ans is None


task1_8_test()

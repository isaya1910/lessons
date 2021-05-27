class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def update_tail(self):
        node = self.head
        self.tail = self.head
        while node is not None:
            self.tail = node
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        ans = []
        while node is not None:
            if node.value == val:
                ans.append(node)
            node = node.next
        return ans

    def delete(self, val, all=False):
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
                if not all:
                    self.update_tail()
                    return
            node = node.next
        self.update_tail()

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        ans = 0
        node = self.head
        while node is not None:
            ans = ans + 1
            node = node.next
        return ans

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.len() == 0:
                self.add_in_head(newNode)
            else:
                self.add_in_tail(newNode)
        else:
            node = self.head
            while node is not None:
                if node is afterNode:
                    buff = node.next
                    node.next = newNode
                    newNode.prev = node
                    if buff is not None:
                        buff.prev = newNode
                    newNode.next = buff
                node = node.next
        self.update_tail()

    def add_in_head(self, newNode):
        node = self.head
        self.head = newNode
        newNode.next = node
        if node is not None:
            node.prev = newNode
        self.update_tail()


def delete_test():
    linked_list = LinkedList2()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(5))
    linked_list.delete(5, False)
    assert linked_list.tail.value == 5

    linked_list.add_in_tail(Node(6))
    linked_list.add_in_tail(Node(7))
    linked_list.add_in_tail(Node(6))
    linked_list.delete(6, True)
    assert linked_list.tail.value == 7
    linked_list.add_in_tail(Node(6))
    linked_list.add_in_tail(Node(6))
    linked_list.delete(6, False)
    assert linked_list.tail.value == 6


def delete_test_2():
    linked_list = LinkedList2()
    linked_list.add_in_tail(Node(3))
    linked_list.add_in_tail(Node(3))
    linked_list.add_in_tail(Node(3))
    linked_list.delete(3, True)
    assert linked_list.len() == 0


def clean_test():
    linked_list = LinkedList2()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(5))
    linked_list.clean()
    assert linked_list.len() == 0


def find_test():
    linked_list = LinkedList2()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(6))
    linked_list.add_in_tail(Node(7))
    assert linked_list.find(7).value == 7
    assert linked_list.find(123) is None


find_test()


def find_all_test():
    linked_list = LinkedList2()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(6))
    linked_list.add_in_tail(Node(7))
    assert len(linked_list.find_all(5)) == 2


find_all_test()


def insert_test():
    linked_list = LinkedList2()
    linked_list.add_in_tail(Node(5))
    linked_list.add_in_tail(Node(5))
    linked_list.insert(linked_list.head.next, Node(6))
    assert linked_list.head.next.next.value == 6
    linked_list.clean()
    linked_list.insert(None, Node(6))
    assert linked_list.head.value == 6
    linked_list.add_in_tail(Node(123))

    linked_list.insert(None, Node(555))
    assert linked_list.tail.value == 555

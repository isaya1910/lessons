import unittest

from mytest2 import LinkedList2, Node


class MyTestCase(unittest.TestCase):

    def test_add_in_head(self):
        linked_list = LinkedList2()
        linked_list.add_in_head(Node(5))
        self.assertEqual(linked_list.get_head().value, 5)
        linked_list.add_in_head(Node(123))
        self.assertEqual(linked_list.get_head().value, 123)

    def test_add_in_tail(self):
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(5))
        self.assertEqual(linked_list.get_tail().value, 5)
        linked_list.add_in_tail(Node(111))
        self.assertEqual(linked_list.get_tail().value, 111)

    def test_delete(self):
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(5))
        linked_list.add_in_tail(Node(6))
        linked_list.add_in_tail(Node(6))
        linked_list.add_in_tail(Node(7))

        self.assertEqual(len(linked_list.find_all(6)), 2)
        linked_list.delete(6, False)
        self.assertEqual(len(linked_list.find_all(6)), 1)

        linked_list.delete(6, False)
        self.assertEqual(len(linked_list.find_all(6)), 0)
        linked_list.add_in_tail(Node(7))
        linked_list.add_in_tail(Node(7))
        self.assertEqual(len(linked_list.find_all(7)), 3)
        linked_list.delete(7, True)
        self.assertEqual(len(linked_list.find_all(7)), 0)

    def test_len(self):
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(5))
        linked_list.add_in_tail(Node(6))
        linked_list.add_in_tail(Node(6))
        linked_list.add_in_tail(Node(7))
        self.assertEqual(linked_list.len(), 4)

        linked_list.delete(6, True)
        linked_list.delete(5, False)
        linked_list.delete(7, False)
        self.assertEqual(linked_list.len(), 0)

    def test_insert(self):
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(5))
        linked_list.add_in_tail(Node(6))
        linked_list.insert(linked_list.get_head().next, Node(123))
        self.assertEqual(linked_list.get_head().next.next.value, 123)
        linked_list.insert(None, Node(123))
        self.assertEqual(linked_list.get_tail().value, 123)
        linked_list.clean()
        linked_list.insert(None, Node(555))
        self.assertEqual(linked_list.get_head().value, 555)
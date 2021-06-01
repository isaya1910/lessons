import unittest

from mytest1 import LinkedList, Node


class Lesson1Test(unittest.TestCase):

    def test_clean(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(5))
        linked_list.add_in_tail(Node(6))
        linked_list.clean()
        self.assertEqual(linked_list.len(), 0)

    def test_find_all(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(5))
        linked_list.add_in_tail(Node(6))
        list = linked_list.find_all(6)
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0].value, 6)

    def test_len(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(5))
        linked_list.add_in_tail(Node(6))
        self.assertEqual(linked_list.len(), 2)

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.add_in_tail(Node(5))
        linked_list.add_in_tail(Node(6))
        linked_list.insert(None, Node(7))
        self.assertEqual(linked_list.head.value, 7)

        linked_list.insert(linked_list.head, Node(5))
        node = linked_list.find(5)
        self.assertIsNotNone(node)
        self.assertIs(linked_list.head.next, node)

import unittest

from mytest1 import LinkedList, Node
from task_1_8 import task1_8


class MyTestCase(unittest.TestCase):
    def test_task1_8(self):
        linked_list1 = LinkedList()
        linked_list1.add_in_tail(Node(6))
        linked_list1.add_in_tail(Node(7))
        linked_list1.add_in_tail(Node(7))

        linked_list2 = LinkedList()
        linked_list2.add_in_tail(Node(6))
        linked_list2.add_in_tail(Node(7))
        linked_list2.add_in_tail(Node(7))

        ans = task1_8(linked_list1, linked_list2)
        self.assertEqual(ans[0], 12)
        linked_list1.add_in_tail(Node(5))
        ans = task1_8(linked_list1, linked_list2)
        self.assertEqual(len(ans), 0)

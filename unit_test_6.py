import unittest

from mytest6 import Deque


class MyTestCase(unittest.TestCase):
    def test_deque(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(2)
        deque.addFront(3)

        self.assertEqual(deque.removeFront(), 3)
        self.assertEqual(deque.removeFront(), 1)
        self.assertEqual(deque.removeFront(), 2)
        self.assertEqual(deque.removeTail(), None)

        deque.addTail(6)
        deque.addTail(5)
        deque.addTail(4)
        deque.addTail(2)
        self.assertEqual(deque.removeFront(), 6)
        self.assertEqual(deque.removeTail(), 2)
        self.assertEqual(deque.size(), 2)

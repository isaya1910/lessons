import unittest

from mytest5 import Queue


class MyTestCase(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), None)

        self.assertEqual(queue.size(), 0)


if __name__ == '__main__':
    unittest.main()

import unittest

from mytest7 import OrderedList
from random import randrange


class MyTestCase(unittest.TestCase):

    def test_ordered_list_increasing_order(self):
        ordered_list = OrderedList(True)
        ordered_list.add(5)
        ordered_list.add(7)
        self.assertEqual(ordered_list.head.value, 5)
        self.assertEqual(ordered_list.tail.value, 7)
        ordered_list.clean(True)
        ordered_list.add(7)
        self.assertEqual(ordered_list.head.value, 7)
        self.assertIsNotNone(ordered_list.tail)
        ordered_list.add(5)
        self.assertEqual(ordered_list.head.value, 5)
        self.assertEqual(ordered_list.tail.value, 7)
        ordered_list.add(1)
        self.assertEqual(ordered_list.head.value, 1)
        self.assertEqual(ordered_list.tail.value, 7)

        ordered_list.add(10)
        self.assertEqual(ordered_list.tail.value, 10)
        ordered_list.add(100)
        self.assertEqual(ordered_list.tail.value, 100)
        ordered_list.add(3)
        print(*ordered_list.get_all_values())

    def test_ordered_list_decreasing_order(self):
        ordered_list = OrderedList(False)
        ordered_list.add(5)
        self.assertEqual(ordered_list.head.value, 5)
        self.assertIsNotNone(ordered_list.tail)
        ordered_list.add(7)
        self.assertEqual(ordered_list.head.value, 7)
        self.assertEqual(ordered_list.tail.value, 5)
        ordered_list.add(2)
        ordered_list.add(12)
        self.assertEqual(ordered_list.head.value, 12)
        self.assertEqual(ordered_list.tail.value, 2)
        ordered_list.add(1)
        self.assertEqual(ordered_list.head.value, 12)
        self.assertEqual(ordered_list.tail.value, 1)

        ordered_list.add(10)
        self.assertEqual(ordered_list.head.next.value, 10)
        ordered_list.add(100)
        self.assertEqual(ordered_list.head.value, 100)
        ordered_list.add(-12)
        ordered_list.add(-16)
        ordered_list.add(18)
        ordered_list.add(20)

        print(*ordered_list.get_all_values())

        #   self.assertEqual(ordered_list.head.next.value, 3)
        print(ordered_list.tail.value)
        print(*ordered_list.get_all_values())

        print(ordered_list.tail.prev.value)
        #    ordered_list.add(99)
        #   self.assertEqual(ordered_list.tail.prev.value, 99)
        print(*ordered_list.get_all_values())
        ordered_list = OrderedList(False)
        n = 100
        list = []
        for i in range(n):
            integer = randrange(1000)
            list.append(integer)
            ordered_list.add(integer)
        print(*list)
        list.sort(reverse=True)
        list_from_ordered_list = ordered_list.get_all_values()
        print(*list)
        print(*ordered_list.get_all_values())

        for k in range(n):
            self.assertEqual(list[k], list_from_ordered_list[k])

        self.assertIsNotNone(ordered_list.tail)
        self.assertIsNotNone(ordered_list.head)

    def test_ordered_list_delete_2(self):
        ordered_list = OrderedList(True)

        ordered_list.add(6)
        ordered_list.add(100)

        ordered_list.delete(100)
        self.assertEqual(ordered_list.head.value, 6)
        self.assertEqual(ordered_list.tail.value, 6)

        ordered_list.add(111)
        self.assertEqual(ordered_list.tail.value, 111)
        ordered_list.add(-1)
        self.assertEqual(ordered_list.head.value, -1)
        ordered_list.delete(-1)
        print(*ordered_list.get_all_values())
        self.assertEqual(ordered_list.head.value, 6)
        self.assertEqual(ordered_list.tail.value, 111)

    def test_delete(self):
        ordered_list = OrderedList(True)
        ordered_list.add(5)
        ordered_list.delete(5)
        self.assertIsNone(ordered_list.head)
        self.assertIsNone(ordered_list.tail)
        ordered_list.add(7)
        ordered_list.add(8)
        ordered_list.add(9)
        ordered_list.delete(9)
        self.assertEqual(ordered_list.tail.value, 8)

    def test_random_ordered_list_delete(self):
        ordered_list = OrderedList(True)
        n = 100
        list = []
        list_do_delete = []
        for i in range(n):
            integer = randrange(1000)
            list.append(integer)
            ordered_list.add(integer)
            if i & 3 == 0:
                list_do_delete.append(integer)

        list.sort()

        for value in list_do_delete:
            ordered_list.delete(value)
            list.remove(value)

        list_from_ordered_list = ordered_list.get_all_values()

        for k in range(len(list)):
            self.assertEqual(list[k], list_from_ordered_list[k])

    def test_ordered_list_len(self):
        ordered_list = OrderedList(True)
        check_list = []
        n = 20

        list_to_delete = []
        for i in range(n):
            integer = randrange(1000)
            ordered_list.add(integer)
            check_list.append(integer)
            if i % 3 == 0:
                list_to_delete.append(integer)
        self.assertEqual(ordered_list.len(), n)
        check_list.sort()

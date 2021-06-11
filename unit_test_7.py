import unittest

from mytest7 import OrderedList
from random import randrange


class MyTestCase(unittest.TestCase):

    def test_ordered_list_increasing_order(self):
        ordered_list = OrderedList(True)
        n = 100
        list = []
        for i in range(n):
            integer = randrange(1000)
            list.append(integer)
            ordered_list.add(integer)
        list.sort()
        list_from_ordered_list = ordered_list.get_all()

        for i in range(n):
            self.assertEqual(list[i], list_from_ordered_list[i].value)

    def test_ordered_list_decreasing_order(self):
        ordered_list = OrderedList(False)
        n = 2
        list = []
        for i in range(n):
            integer = randrange(1000)
            list.append(integer)
            ordered_list.add(integer)
            self.assertIsNotNone(ordered_list.head)

        self.assertIsNotNone(ordered_list.tail)
        list.sort(reverse=True)
        list_from_ordered_list = ordered_list.get_all()

        for k in range(n):
            self.assertEqual(list[k], list_from_ordered_list[k].value)

        self.assertIsNotNone(ordered_list.tail)
        self.assertIsNotNone(ordered_list.head)

    def test_ordered_list_delete(self):
        ordered_list = OrderedList(False)
        n = 100
        list = []
        for i in range(n):
            integer = randrange(1000)
            list.append(integer)
            ordered_list.add(integer)
        list.sort(reverse=True)
        list_from_ordered_list = ordered_list.get_all()
        for k in range(n):
            self.assertEqual(list[k], list_from_ordered_list[k].value)

        ordered_list.delete(list[25])

        list.remove(list[25])
        ordered_list.delete(list[0])
        list.remove(list[0])

        list_from_ordered_list = ordered_list.get_all()

        for k in range(len(list)):
            self.assertEqual(list[k], list_from_ordered_list[k].value)

    def test_ordered_list_len(self):
        ordered_list = OrderedList(False)
        n = 1000

        list_to_delete = []
        for i in range(n):
            integer = randrange(1000)
            ordered_list.add(integer)
            if i % 3 == 0:
                list_to_delete.append(integer)
        self.assertEqual(ordered_list.len(), n)

        for i in range(len(list_to_delete)):
            ordered_list.delete(list_to_delete[i])
        self.assertEqual(ordered_list.len(), n - len(list_to_delete))
        ordered_list.clean(False)
        self.assertEqual(ordered_list.len(), 0)

        n = 100
        list = []
        for i in range(n):
            integer = randrange(1000)
            list.append(integer)
            ordered_list.add(integer)
        list.sort(reverse=True)
        list_from_ordered_list = ordered_list.get_all()

        for k in range(n):
            self.assertEqual(list[k], list_from_ordered_list[k].value)

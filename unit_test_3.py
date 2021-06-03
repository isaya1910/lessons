import unittest

from mytest3 import DynArray


class MyTestCase(unittest.TestCase):

    def test_when_capacity_did_not_raised(self):
        array = DynArray()
        self.assertEqual(array.capacity, 16)
        for i in range(16):
            array.append(1)
        self.assertEqual(array.capacity, 16)

    def test_when_capacity_raised(self):
        array = DynArray()
        self.assertEqual(array.capacity, 16)
        for i in range(20):
            array.append(1)
        self.assertEqual(array.__getitem__(len(array) - 1), 1)
        self.assertEqual(array.capacity, 32)

    def test_delete_when_capacity_did_not_decreased(self):
        array = DynArray()
        self.assertEqual(array.capacity, 16)
        for i in range(48):
            array.append(1)
        self.assertEqual(array.capacity, 64)
        array.delete(0)
        self.assertEqual(array.capacity, 64)

    def test_delete_when_capacity_decreased(self):
        array = DynArray()
        self.assertEqual(array.capacity, 16)
        for i in range(48):
            array.append(1)
        self.assertEqual(array.capacity, 64)
        for i in range(20):
            array.delete(0)
        self.assertLess(array.capacity, 64)

    def test_insert_to_the_bad_position(self):
        array = DynArray()
        with self.assertRaises(IndexError):
            array.insert(1, 1)

    def test_delete_to_the_bad_position(self):
        array = DynArray()
        with self.assertRaises(IndexError):
            array.delete(1)

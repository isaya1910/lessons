import unittest

from mytes10 import PowerSet


class MyTestCase(unittest.TestCase):
    def test_set(self):
        set = PowerSet()
        self.assertEqual(set.get("asd"), False)

        set.put("asd")
        self.assertEqual(set.get("asd"), True)
        set.remove("asd")
        self.assertEqual(set.get("asd"), False)
        set.put("sss")
        self.assertEqual(set.size(), 1)
        self.assertEqual(set.remove("sss"), True)

        self.assertEqual(set.remove("sss"), False)

    def test_4(self):
        a = {1}
        b = {1, 2, 3}
        print(b.issubset(a))
        print(a.issubset(b))
        a = set()
        print(a.issubset(b))
        print(b.issubset(a))

    def test_3_set(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set1.put(3)
        self.assertEqual(set1.issubset(set2), True)
        self.assertEqual(set2.issubset(set1), False)

        set1.union(set2).print()
        set2.put(3)
        set1.difference(set2).print()
        self.assertEqual(set1.issubset(set2), True)
        self.assertEqual(set2.issubset(set1), True)

    def test_2_set(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(100):
            if i % 3 == 0:
                set1.put(4)
            else:
                set1.put(6)
        for i in range(50):
            if i % 3 == 0:
                set2.put(123)
            else:
                set2.put(4)

        set1.difference(set2).print()
        set1.intersection(set2).print()
        set1.union(set2).print()
        self.assertEqual(set1.issubset(set2), False)
        self.assertEqual(set2.issubset(set1), False)

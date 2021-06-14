import unittest

from mytest8 import HashTable


class MyTestCase(unittest.TestCase):
    def test_hash_fun(self):
        self.assertEqual(9, 9)
        hash_table = HashTable(19, 3)

        for i in "qwertyuiopasdfghjklzxcvbnm":
            print((hash_table.hash_fun(i)))

    def test_find(self):
        hash_table = HashTable(19, 3)
        hash_table.put("www")
        hash_table.put("ddd")
        index1 = hash_table.find("www")
        index2 = hash_table.find("ddd")

        self.assertEqual(index1, 0)
        self.assertEqual(index2, 3)
        self.assertEqual(hash_table.find("dsasd"), None)

    def test_put(self):
        hash_table = HashTable(19, 3)
        for i in "qwertyuiopasdfghjklzxcvbnm":
            hash_table.put(i)
        self.assertIsNone(hash_table.seek_slot("m"), None)

    def test_seek_slut(self):
        hash_table = HashTable(19, 3)
        ss = hash_table.seek_slot("www")
        print(ss)
        hash_table.put("www")
        hash_table.put("ddd")
        index_1 = hash_table.seek_slot("www")
        index_2 = hash_table.seek_slot("ddd")

        index_3 = hash_table.seek_slot("eee")

        self.assertEqual(index_1, 0)
        self.assertEqual(index_2, 3)
        self.assertEqual(index_3, 6)

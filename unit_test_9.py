import unittest

from mytest9 import NativeDictionary


class MyTestCase(unittest.TestCase):
    def test_is_key(self):
        dict = NativeDictionary(100)
        self.assertEqual(dict.is_key("asd"), False)
        dict.put("asd", 123)
        self.assertEqual(dict.is_key("asd"), True)
        value = dict.get("asd")
        self.assertEqual(value, 123)
        value2 = dict.get("ddd")
        self.assertEqual(value2, None)
        dict.put("ddd", 999)
        value2 = dict.get("ddd")
        self.assertEqual(value2, 999)
        self.assertEqual(dict.is_key("vvv"), False)
        dict.put("vvv", 123)
        self.assertEqual(dict.is_key("vvv"), True)
        self.assertEqual(dict.get("vvv"), 123)

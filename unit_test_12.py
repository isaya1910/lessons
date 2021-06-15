import unittest

import unittest

from mytest12 import NativeCache
from mytest9 import NativeDictionary


class MyTestCase(unittest.TestCase):
    def test_is_key(self):
        dict = NativeCache(100)
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
        self.assertEqual(dict.is_key("eee"), False)
        self.assertEqual(dict.is_key("rrr"), False)
        dict.put("ddd", 1233)
        self.assertEqual(dict.is_key("ddd"), True)
        self.assertEqual(dict.get("ddd"), 1233)

        self.assertEqual(dict.is_key("vvv"), True)
        self.assertEqual(dict.get("vvv"), 123)


if __name__ == '__main__':
    unittest.main()

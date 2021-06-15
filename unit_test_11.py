import unittest

from mytest11 import BloomFilter


class MyTestCase(unittest.TestCase):
    def test(self):
        bloom_filter = BloomFilter(32)
        self.assertEqual(bloom_filter.is_value("0123456789"), False)

        bloom_filter.add("0123456789")

        self.assertEqual(bloom_filter.is_value("0123456789"), True)
        self.assertEqual(bloom_filter.is_value("1234567890"), False)
        bloom_filter.add("1234567890")
        self.assertEqual(bloom_filter.is_value("1234567890"), True)
        self.assertEqual(bloom_filter.is_value("2345678901"), False)
        bloom_filter.add("2345678901")
        self.assertEqual(bloom_filter.is_value("2345678901"), True)


if __name__ == '__main__':
    unittest.main()

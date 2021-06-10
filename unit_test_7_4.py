import unittest

from mytest7 import OrderedStringList


class MyTestCase(unittest.TestCase):
    def test_ordered_string_list(self):
        ordered_string_list = OrderedStringList(True)
        ordered_string_list.add("aaaaa")
        ordered_string_list.add("a      ")

        ordered_string_list.add("asd   ")
        ordered_string_list.add("   aaa")

        ordered_string_list.add("bbb")

        node = ordered_string_list.head
        while node is not None:
            print(node.value)
            node = node.next



if __name__ == '__main__':
    unittest.main()

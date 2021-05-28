import unittest

from mytest3 import DynArray


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_delete_dynamic_array(self):
        array = DynArray()
        for i in range(40):
            array.append(20)

        print(*array)
        print(array.capacity)

        for i in range(38):
            array.delete(0)

        print(*array)
        print(array.capacity)


if __name__ == '__main__':
    unittest.main()

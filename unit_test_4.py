import unittest

from mytest4 import Stack


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_stack(self):
        stack = Stack()
        stack.push(123)
        stack.push(455)
        self.assertEqual(stack.pop(), 455)
        self.assertEqual(stack.pop(), 123)
        stack.push(11)
        self.assertEqual(stack.peek(), 11)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), 11)
        self.assertEqual(stack.pop(), None)

    def test_stack_scopes(self):
        stack = Stack()

        test_string = "()(())"
        ans = True
        for c in test_string:
            if c == '(':
                stack.push(c)
            if c == ')':
                scope = stack.pop()
                if scope is None:
                    ans = False
                    break
        if stack.size() > 0:
            ans = False

        self.assertEqual(ans, True)


if __name__ == '__main__':
    unittest.main()

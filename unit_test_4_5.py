import unittest

from mytest4 import Stack
from task_4_5 import is_scopes_balance, polish_notation


class MyTestCase(unittest.TestCase):

    def test_stack_scopes(self):
        test_string = "()(())"
        self.assertEqual(is_scopes_balance(test_string), True)
        test_string2 = "(((()("
        self.assertEqual(is_scopes_balance(test_string2), False)

    def test_polish(self):
        polish = "8 2 + 5 * 9 +"
        self.assertEqual(polish_notation(polish), 59)
        polish = "1 2 + 3 *"
        self.assertEqual(polish_notation(polish), 9)

import unittest
import class_example

class Test(unittest.TestCase):
    def setup(self):
        return
    def test_divide(self):
        first = 4
        second = 2
        result = class_example.divide(first, second)

        expect = 2

        self.assertEqual(result, expect)
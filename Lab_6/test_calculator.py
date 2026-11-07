import unittest
from calculator import calculate_discount

class TestCalculator(unittest.TestCase):

    def test_member_expensive_item(self):
        self.assertEqual(calculate_discount(150, True), 127.5)

    def test_non_member_expensive_item(self):
        self.assertEqual(calculate_discount(150, False), 142.5)

    def test_member_cheap_item(self):
        self.assertEqual(calculate_discount(80, True), 72)

    def test_non_member_cheap_item(self):
        self.assertEqual(calculate_discount(80, False), 80)


if __name__ == '__main__':
    unittest.main()
import unittest
from calculator import calculate_discount

class TestBranchCoverage(unittest.TestCase):

    def test_member_true(self):
        self.assertEqual(calculate_discount(150, True), 127.5)

    def test_member_false(self):
        self.assertEqual(calculate_discount(150, False), 142.5)

    def test_price_above_100(self):
        self.assertEqual(calculate_discount(150, True), 127.5)

    def test_price_below_100(self):
        self.assertEqual(calculate_discount(80, True), 72)

    def test_price_equal_100(self):
        self.assertEqual(calculate_discount(100, False), 100)

if __name__ == '__main__':
    unittest.main()
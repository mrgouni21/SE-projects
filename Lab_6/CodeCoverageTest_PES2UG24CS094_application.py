import unittest
from calculator import calculate_discount

class TestCodeCoverage(unittest.TestCase):

    def test_member_expensive(self):
        self.assertEqual(calculate_discount(150, True), 127.5)

    def test_nonmember_expensive(self):
        self.assertEqual(calculate_discount(150, False), 142.5)

    def test_member_cheap(self):
        self.assertEqual(calculate_discount(80, True), 72)

    def test_nonmember_cheap(self):
        self.assertEqual(calculate_discount(80, False), 80)

if __name__ == '__main__':
    unittest.main()
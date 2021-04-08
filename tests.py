import unittest

from sumFunction import mySum


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(mySum(1, 2), 3, "Should be three")


if __name__ == '__main__':
    unittest.main()

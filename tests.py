import unittest

from sumFunction import mySum, divide,secondItemInList


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(mySum(1, 2), 3, "Should be three")
    def test_divide(self):
        self.assertEqual(divide(4,2),2,"Should be 2")
    def test_list(self):
        myList=[1,2,3,4,5]
        self.assertEqual(secondItemInList(myList),2,"Should be 2")
     


if __name__ == '__main__':
    unittest.main()

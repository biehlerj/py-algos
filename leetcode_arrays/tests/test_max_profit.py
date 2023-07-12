import unittest

from leetcode_arrays.max_profit.max_profit import maxProfit


class TestMaxProfit(unittest.TestCase):
    test_arrays = [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
    test_outputs = [7, 4, 0]

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("......  For Best Time to  .......")
        print("...... Buy and Sell Stock .......")
        print(".................................\n\n")

    def test_max_profit(self):
        for i in range(len(self.test_arrays)):
            self.assertEqual(maxProfit(self.test_arrays[i]), self.test_outputs[i])


if __name__ == '__main__':
    unittest.main()

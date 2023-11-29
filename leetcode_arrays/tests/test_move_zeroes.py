import unittest

from leetcode_arrays.move_zeroes.move_zeroes import moveZeroes


class TestMoveZeroes(unittest.TestCase):
    test_arrays = [[0, 1, 0, 3, 12], [0]]
    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("......  For Moving Zeroes  ......")
        print(".......... in an Array ..........")
        print(".................................\n\n")
    def test_move_zeroes(self):
        for i in range(len(self.test_arrays)):
            self.assertIsNone(moveZeroes(self.test_arrays[i]))


if __name__ == '__main__':
    unittest.main()

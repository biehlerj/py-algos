import unittest

from leetcode_arrays.plus_one.plus_one import plusOne


class TestPlusZero(unittest.TestCase):
    test_arrays = [[1, 2, 3], [4, 3, 2, 1], [9]]
    test_output_arrays = [[1, 2, 4], [4, 3, 2, 2], [1, 0]]

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("......  For Adding One to  ......")
        print("........ Array of digits ........")
        print(".................................\n\n")

    def test_something(self):
        for i in range(len(self.test_arrays)):
            self.assertEqual(plusOne(self.test_arrays[i]), self.test_output_arrays[i])


if __name__ == '__main__':
    unittest.main()

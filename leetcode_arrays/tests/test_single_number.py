import unittest

from leetcode_arrays.single_number.single_number import singleNumber


class TestSingleNumber(unittest.TestCase):
    test_arrays = [[2, 2, 1], [4, 1, 2, 1, 2], [1]]
    test_outputs = [1, 4, 1]

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("..  For Finding Single Number  ..")
        print(".......... in an Array ..........")
        print(".................................\n\n")

    def test_something(self):
        for i in range(len(self.test_arrays)):
            self.assertEqual(singleNumber(self.test_arrays[i]), self.test_outputs[i])


if __name__ == '__main__':
    unittest.main()

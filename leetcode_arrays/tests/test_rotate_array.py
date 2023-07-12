import unittest

from leetcode_arrays.rotate_array.rotate_array import rotate


class TestRotateArray(unittest.TestCase):
    test_arrays = [[1, 2, 3, 4, 5, 6, 7], [-1, -100, 3, 99]]
    test_rotates = [3, 2]
    test_outputs = [[5, 6, 7, 1, 2, 3, 4], [3, 99, -1, -100]]

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("....  For Rotating an Array  ....")
        print(".................................\n\n")

    def test_rotate(self):
        for i in range(len(self.test_arrays)):
            self.assertIsNone(rotate(self.test_arrays[i], self.test_rotates[i]))


if __name__ == '__main__':
    unittest.main()

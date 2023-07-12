import unittest

from leetcode_arrays.remove_dupes.remove_dupes import removeDuplicates


class TestRemoveDupes(unittest.TestCase):
    test_arrays = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    test_outputs = [2, 5]

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("...  For Removing duplicates  ...")
        print("....... from Sorted Array .......")
        print(".................................\n\n")

    def test_remove_dupes(self):
        for i in range(len(self.test_arrays)):
            self.assertEqual(removeDuplicates(self.test_arrays[i]), self.test_outputs[i])


if __name__ == '__main__':
    unittest.main()

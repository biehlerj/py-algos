import unittest

from leetcode_arrays.contains_dupe.contains_dupe import containsDuplicate


class TestContainsDupe(unittest.TestCase):
    test_arrays = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
    test_outputs = [True, False, True]

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("....  For Finding duplicates  ...")
        print(".......... in an Array ..........")
        print(".................................\n\n")

    def test_contains_duplicate(self):
        for i in range(len(self.test_arrays)):
            self.assertEqual(containsDuplicate(self.test_arrays[i]), self.test_outputs[i])


if __name__ == '__main__':
    unittest.main()

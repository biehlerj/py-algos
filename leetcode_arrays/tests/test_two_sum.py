import unittest


class TestTwoSum(unittest.TestCase):
    test_arrays = [[2,7,11,15],[3,2,4],[3,3]]
    test_output_arrays = [[0,1],[1,2],[0,1]]
    test_targets = [9, 6, 6]

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("......  For Finding Sum  ......")
        print(".......... in an Array ..........")
        print(".................................\n\n")
    def test_two_sum(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

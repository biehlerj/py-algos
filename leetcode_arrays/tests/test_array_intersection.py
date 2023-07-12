import unittest

from leetcode_arrays.array_intersection.array_intersection import intersect


class TestArrayIntersection(unittest.TestCase):
    test_arrays1 = [[1, 2, 2, 1], [4, 9, 5]]
    test_arrays2 = [[2, 2], [9, 4, 9, 8, 4]]
    test_output_arrays = [[2, 2], [9, 4]]

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("...  For Finding Intersection  ..")
        print("......... of Two Arrays .........")
        print(".................................\n\n")

    def test_something(self):
        for i in range(len(self.test_arrays1)):
            self.assertEqual(intersect(self.test_arrays1[i], self.test_arrays2[i]), self.test_output_arrays[i])


if __name__ == '__main__':
    unittest.main()

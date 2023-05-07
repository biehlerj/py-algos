from linear_search.linear_search import linear_search
import unittest


class TestLinearSearch(unittest.TestCase):
    test_array = [2, 3, 4, 10, 40]

    @classmethod
    def setUpClass(cls) -> None:
        print("\n\n.................................")
        print("..... Testing Functionality .....")
        print("......  For Linear Search  ......")
        print(".................................\n\n")

    def test_good_search(self):
        target = 10
        result = linear_search(self.test_array, len(self.test_array), target)
        self.assertEqual(result, 3)

    def test_bad_search(self):
        target = 69
        result = linear_search(self.test_array, len(self.test_array), target)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    """
    Main Tests
    """
    unittest.main

from linear_search.linear_search import linear_search
import inspect
import pep8
import unittest


class TestLinearSearchDocs(unittest.TestCase):
    all_funcs = inspect.getmembers(linear_search, inspect.isfunction)

    @classmethod
    def setUpClass(cls):
        print("\n\n.................................")
        print("..... Testing Documentation .....")
        print("......  For Linear Search  ......")
        print(".................................\n\n")

    def test_doc_file(self):
        actual = linear_search.__doc__
        self.assertIsNotNone(actual)

    def test_all_function_docs(self):
        all_functions = TestLinearSearchDocs.all_funcs
        for function in all_functions:
            self.assertIsNotNone(function[1].__doc__)

    def test_pep8(self):
        pep8_style = pep8.StyleGuide(quiet=True)
        errors = pep8_style.check_files(["linear_search/linear_search.py"])
        self.assertEqual(errors.total_errors, 0, errors.messages)


if __name__ == "__main__":
    """
    Main Tests
    """
    unittest.main

# pylint: disable-all
import unittest
from .search_engine import search_engine

class TestFactorial(unittest.TestCase):
    """
    Test class
    """

    def test_reordering_of_a_list(self):
        """
        Test the reordering of a list
        """
        actual = search_engine.iterate_through_dict({"test":"1", "test":"3"})
        expected = {"test":"3", "test":"1"}
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
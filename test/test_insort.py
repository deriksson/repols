import unittest
from test.list_item import ListItem

from repols.insort import insort_any_type_left


class TestInsort(unittest.TestCase):
    def test_inserting_int_into_empty_list(self):
        ordered_list = []
        for repo in [3, 2, 1]:
            insort_any_type_left(ordered_list, repo)
        self.assertEqual([1, 2, 3], ordered_list)

    def test_inserting_object_into_empty_list(self):
        def less_than(lhs, rhs):
            return lhs.value < rhs.value

        ordered_list = []
        for repo in [ListItem(3), ListItem(2), ListItem(1)]:
            insort_any_type_left(ordered_list, repo, less_than)

        self.assertEqual([ListItem(1), ListItem(2), ListItem(3)], ordered_list)


if __name__ == "__main__":
    unittest.main()

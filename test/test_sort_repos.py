import unittest
from test.list_item import ListItem

from repols.list_repositories import sorted_repos


class TestSortRepos(unittest.TestCase):
    def test_list_of_repositories_is_sorted(self):
        field = "archived"
        available_fields = {
            field: lambda repo: str(repo.value),
        }
        team_repos = [ListItem(3), ListItem(2), ListItem(1)]

        self.assertEqual(
            [ListItem(1), ListItem(2), ListItem(3)],
            sorted_repos(team_repos, available_fields, field),
        )


if __name__ == "__main__":
    unittest.main()

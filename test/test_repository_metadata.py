import unittest
from test.list_item import ListItem

from repols.list_repositories import repo_metadata


class TestRepositoryMetadata(unittest.TestCase):
    def test_metadata_is_retrieved(self):
        included_fields = ("name", "archived")
        available_fields = {
            "archived": lambda repo: str(repo.value),
            "name": lambda repo: "a-repository-name",
        }
        self.assertEqual(
            ["a-repository-name", "1"],
            repo_metadata(
                included_fields,
                available_fields,
                lambda field: available_fields[field](ListItem(1)),
            ),
        )


if __name__ == "__main__":
    unittest.main()

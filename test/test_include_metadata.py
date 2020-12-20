import unittest

from repols.list_repositories import repo_metadata


class TestIncludeMetadata(unittest.TestCase):
    def test_get_archived_value(self):
        available_fields = {"archived": lambda repo: "True"}
        self.assertEqual(["True"], repo_metadata(("archived",), available_fields, None))

    def test_get_metadata(self):
        available_fields = {
            "archived": lambda repo: "True",
            "created_at": lambda repo: "2020-01-01T12:00",
        }
        self.assertEqual(
            ["True", "2020-01-01T12:00"],
            repo_metadata(("archived", "created_at"), available_fields, None),
        )

    def test_non_existing_field(self):
        available_fields = {
            "archived": lambda repo: "True",
            "created_at": lambda repo: "2020-01-01T12:00",
        }
        self.assertEqual(
            ["True", "2020-01-01T12:00"],
            repo_metadata(("archived", "created_at", "name"), available_fields, None),
        )


if __name__ == "__main__":
    unittest.main()

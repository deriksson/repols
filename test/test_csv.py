import unittest

from repols.csv import quote


class TestCsv(unittest.TestCase):
    def test_embedded_comma(self):
        self.assertEqual('"a,b"', quote("a,b"))

    def test_simple_field(self):
        self.assertEqual("a", quote("a"))


if __name__ == "__main__":
    unittest.main()

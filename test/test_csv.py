import unittest


from repols.csv import quote, escape


class TestCsv(unittest.TestCase):
    def test_embedded_comma(self):
        self.assertEqual('"a,b"', quote("a,b"))

    def test_simple_field(self):
        self.assertEqual("a", quote("a"))

    def test_escape_quote(self):
        self.assertEqual('""', escape('"'))

    def test_embedded_quote(self):
        self.assertEqual('"""a"""', quote('"a"'))


if __name__ == "__main__":
    unittest.main()

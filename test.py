import unittest
from main import parse


class TestParse(unittest.TestCase):

    def test_correct_1(self):
        actual = parse('https://example.com/path/to/page?name=ferret&color=purple')
        expected = {'name': 'ferret', 'color': 'purple'}
        self.assertEqual(actual, expected)

    def test_correct_2(self):
        actual = parse('https://example.com/path/to/page?name=ferret&color=purple&')
        expected = {'name': 'ferret', 'color': 'purple'}
        self.assertEqual(actual, expected)

    def test_empty_1(self):
        actual = parse('http://example.com/')
        expected = {}
        self.assertEqual(actual, expected)

    def test_empty_2(self):
        actual = parse('http://example.com/?')
        expected = {}
        self.assertEqual(actual, expected)

    def test_one_property(self):
        actual = parse('http://example.com/?name=Dima')
        expected = {'name': 'Dima'}
        self.assertEqual(actual, expected)

    def test_cyrillic(self):
        actual = parse('https://example.com/path/to/page?name=жук&color=зелений')
        expected = {'name': 'жук', 'color': 'зелений'}
        self.assertEqual(actual, expected)

    def test_symbol(self):
        actual = parse('https://example.com/path/to/page?name=ferret==&color=purple!!')
        expected = {'name': 'ferret==', 'color': 'purple!!'}
        self.assertEqual(actual, expected)

    def test_empty_value(self):
        actual = parse('http://example.com/?name=')
        expected = {}
        self.assertEqual(actual, expected)

    def test_whitespace_value(self):
        actual = parse('http://example.com/?name= ')
        expected = {'name': ' '}
        self.assertEqual(actual, expected)

    def test_whitespace_key(self):
        actual = parse('http://example.com/? =Dima ')
        expected = {' ': 'Dima '}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

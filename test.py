import unittest
from main import parse_cookie


class TestParseCookie(unittest.TestCase):

    def test_correct(self):
        actual = parse_cookie('name=Dima;')
        expected = {'name': 'Dima'}
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = parse_cookie('')
        expected = {}
        self.assertEqual(actual, expected)

    def test_two_items(self):
        actual = parse_cookie('name=Dima;age=28;')
        expected = {'name': 'Dima', 'age': '28'}
        self.assertEqual(actual, expected)

    def test_value_with_equals_symbol(self):
        actual = parse_cookie('name=Dima=User;age=28;')
        expected = {'name': 'Dima=User', 'age': '28'}
        self.assertEqual(actual, expected)

    def test_three_items(self):
        actual = parse_cookie('name=Dima=User;age=28;role=student')
        expected = {'name': 'Dima=User', 'age': '28', 'role': 'student'}
        self.assertEqual(actual, expected)

    def test_cyrillic(self):
        actual = parse_cookie('name=Богдан ;age= ;')
        expected = {'name': 'Богдан ', 'age': ' '}
        self.assertEqual(actual, expected)

    def test_symbol_value(self):
        actual = parse_cookie('name=!=+;age=12;')
        expected = {'name': '!=+', 'age': '12'}
        self.assertEqual(actual, expected)

    def test_empty_value(self):
        actual = parse_cookie('name=;age=22;')
        expected = {'name': '', 'age': '22'}
        self.assertEqual(actual, expected)

    def test_empty_item(self):
        actual = parse_cookie('name=Dima;;age=28;')
        expected = {'name': 'Dima', 'age': '28'}
        self.assertEqual(actual, expected)

    def test_incorrect_item(self):
        actual = parse_cookie('name=Dima;a;age=28;')
        expected = {'name': 'Dima', 'age': '28'}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
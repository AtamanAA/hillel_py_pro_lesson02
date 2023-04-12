import unittest
from main import parse_cookie
from main import parse


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

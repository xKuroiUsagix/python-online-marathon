import unittest
from unittest.mock import mock_open, patch


def file_parser(filename: str, find_s: str, replace_s=None):
    with open(filename) as file:
        data = file.read()

    count = data.count(find_s)
    if replace_s is None:
        return f'Found {count} strings'

    replaced = data.replace(find_s, replace_s)
    with open(filename, 'w') as file:
        file.write(replaced)
    return f'Replaced {count} strings'


class ParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = """
        This is string for testing.
        It's imitate a content of some file.txt
        """
        self.to_find = 'ing'

    def test_count_substrings(self):
        expected = 'Found 2 strings'
        with patch('builtins.open',
                   mock_open(read_data=self.text)) as mock_file:
            open('path/to/open').read() == 'file.txt'
            mock_file.assert_called_with('path/to/open')
            self.assertEqual(file_parser(mock_file, self.to_find), expected)

    def test_replace_substrings(self):
        expected = 'Replaced 2 strings'
        to_replace = 'abc'
        with patch('builtins.open',
                   mock_open(read_data=self.text)) as mock_file:
            open('path/to/open').read() == 'file.txt'
            mock_file.assert_called_with('path/to/open')
            self.assertEqual(file_parser(mock_file,
                                         self.to_find,
                                         to_replace), expected)

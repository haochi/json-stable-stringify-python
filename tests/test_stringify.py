import unittest
from .context import json_stable_stringify_python as stringify

class TestStringify(unittest.TestCase):
    def test_simple_object(self):
        node = {'c':6, 'b': [4,5], 'a': 3, 'z': None}
        actual = stringify.stringify(node)
        expected = '{"a":3,"b":[4,5],"c":6,"z":null}'
        self.assertEqual(actual, expected)

    def test_object_with_empty_string(self):
        node = {'a': 3, 'z': ''}
        actual = stringify.stringify(node)
        expected = '{"a":3,"z":""}'
        self.assertEqual(actual, expected)

    def test_nested_object(self):
        node = {
            'a': {
                'b': {
                    'c': [1,2,3,None]
                }
            }
        }
        actual = stringify.stringify(node)
        expected = '{"a":{"b":{"c":[1,2,3,null]}}}'
        self.assertEqual(actual, expected)

    def test_array_with_none(self):
        node = [1, None]
        actual = stringify.stringify(node)
        expected = '[1,null]'
        self.assertEqual(actual, expected)

    def test_array_with_empty_string(self):
        node = [1, '']
        actual = stringify.stringify(node)
        expected = '[1,""]'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

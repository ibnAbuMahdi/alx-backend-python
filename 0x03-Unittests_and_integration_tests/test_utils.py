#!/usr/bin/env python3
""" test1 - parameterize, access_nested_map """
from unittest import (TestCase, mock)
from utils import (get_json, access_nested_map, memoize)
from typing import (Mapping, Sequence, Any)
from parameterized import parameterized
import requests


class TestAccessNestedMap(TestCase):
    """ class that tests nested map Mapping """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
            ])
    def test_access_nested_map(
            self, nest_map: Mapping,
            path: Sequence,
            expected: Any
            ) -> None:
        """ tests access nested map """
        self.assertEqual(access_nested_map(nest_map, path), expected)

    @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
            ])
    def test_access_nested_map_exception(
            self, nest_map: Mapping,
            path: Sequence
            ) -> None:
        """ tests access nested map for KeyError """
        with self.assertRaises(KeyError) as cm:
            err = access_nested_map(nest_map, path)
            self.assertEqual(cm.exception, str(err))


class TestGetJson(TestCase):
    """ class that tests get json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url: str, payload: Mapping) -> None:
        """ test get json method """
        with mock.patch('requests.get') as mo:
            mr: Any = mo.return_value
            mr.json.return_value = payload
            data: Mapping = get_json(url)
            self.assertEqual(data, payload)
        mo.assert_called_once_with(url)


class TestMemoize(TestCase):
    """ tests moization class """
    def test_memoize(self):
        """ tests moization of function calls """
        class TestClass:
            """ test class of test_moize """

            def a_method(self):
                """ a method to test memoization """
                return 42

            @memoize
            def a_property(self):
                """ a property in test class of test_memoize """
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method', return_value=42) as mm:
            tc: TestClass = TestClass()
            tc.a_property
            self.assertEqual(tc.a_property, 42)
        mm.assert_called_once()


if __name__ == '__main__':
    unittest.main()

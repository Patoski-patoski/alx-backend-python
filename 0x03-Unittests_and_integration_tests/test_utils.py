#!/usr/bin/env python3
"""test_utils.py"""

import unittest
from parameterized import parameterized
from typing import Any, Mapping, Sequence, Dict
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap: test that the method returns what it is
    supposed to.
    Args:
        unittest (TestCase): Base case
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
             self, n_map: Mapping, path: Sequence, expected: Any):
        """Test that access_nested_map returns the correct value.
        Args:
            n_map (Mapping): map
            path (Sequence): path
            expected (Any): output
        """
        self.assertEqual(access_nested_map(n_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b')),
    ])
    def test_access_nested_map_exception(
            self, n_map: Mapping, path: Sequence, expected: Any):
        """Test that a KeyError is raised for the following inputs"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(n_map, path)

        self.assertEqual(str(context.exception), f"{expected}")


class TestGetJson(unittest.TestCase):
    """TestGetJson: test and returns Mock HTTP calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """test_get_json:to test that utils.get_json returns expected result"""

        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        with patch("utils.requests.get", return_value=mock_resp) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()

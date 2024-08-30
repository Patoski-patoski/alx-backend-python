#!/usr/bin/env python3
"""test_client module"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for GithubOrgClient class"""
    @parameterized.expand([
        'google',
        'abc',
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json):
        """test that GithubOrgClient.org returns the correct value."""
        # prepare the mock return value
        expected_payload = {'org_name': org_name}
        mock_get_json.return_value = expected_payload
        # create instance of GithubOrgClient
        client = GithubOrgClient(org_name)
        # call the org method
        result = client.org
        # Assert that get_json was called once with the correct URL
        # org_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        mock_get_json.assert_called_once_with(org_url)
        self.assertEqual(result, expected_payload)

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    def test_public_repos_url(self, org_name, expected_org_url: str):
        """generates the puplic url for org_name"""

        # Prepare the mock return value for the org property
        payload = {"repos_url": expected_org_url}

        # Patch GithubOrgClient.org to return the payload
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock, return_value=payload):
            # create instance of GithubOrgClient
            client = GithubOrgClient(org_name)

            # call the _public_repos_url method
            result = client._public_repos_url

            # Assert that get_json was called once with the correct URL
            self.assertEqual(result, expected_org_url)


if __name__ == "__main__":
    unittest.main()

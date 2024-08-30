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
        org_url = f"https://api.github.com/orgs/{org_name}"
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns correct list of repos
        """
        # Example payload returned by get_json
        example_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl-3.0"}},
        ]

        # Expected repo names from the payload
        expected_repos = ["repo1", "repo2", "repo3"]

        # Mock get_json to return the example payload
        mock_get_json.return_value = example_repos_payload

        # Mock _public_repos_url to return a fake URL
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://fake.url/repos"

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test_org")

            # Call the public_repos method
            repos = client.public_repos()

            # Assert the returned repo list is as expected
            self.assertEqual(repos, expected_repos)

            # Assert _public_repos_url was called once
            mock_public_repos_url.assert_called_once()

            # Assert get_json was called once with the fake URL
            mock_get_json.assert_called_once_with("https://fake.url/repos")


if __name__ == "__main__":
    unittest.main()

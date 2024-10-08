#!/usr/bin/env python3
"""test_client module"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json):
        """test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        client.org()
        org_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(org_url)

    @patch("client.get_json")
    def test_public_repos_url(self, mock_get_json):
        """Unit-test for GithubOrgClient.public_repos method"""

        # Prepare the mock return value for the org property
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        # Patch GithubOrgClient.org to return the payload
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_public_repos_url:
            url = "https://api.github.com/orgs/test-org/repos"
            mock_public_repos_url.return_value = url
            client = GithubOrgClient("test-org")
            repos = client.public_repos()

            # Test that the list of repos is correct
            self.assertEqual(repos, ["repo1", "repo2"])

            # Test that the mocked property was called once
            mock_public_repos_url.assert_called_once()

            # Test that the mocked get_json was called once
            mock_get_json.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns correct list of
        repos"""
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
        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_pub_rep_url:
            mock_pub_rep_url.return_value = "https://fake.url/repos"

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test_org")

            # Call the public_repos method
            repos = client.public_repos()

            # Assert the returned repo list is as expected
            self.assertEqual(repos, expected_repos)

            # Assert _public_repos_url was called once
            mock_pub_rep_url.assert_called_once()

            # Assert get_json was called once with the fake URL
            mock_get_json.assert_called_once_with("https://fake.url/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Edge case where the repo has no license
        ({"license": None}, "my_license", False),
        # Edge case where the license is None
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns the correct boolean
        value."""

        # Call the has_license method
        result = GithubOrgClient.has_license(repo, license_key)

        # Assert that the result matches the expected value
        self.assertEqual(result, expected)

    @patch("client.get_json")
    @patch.object(GithubOrgClient, "_public_repos_url",
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_pub_rep_url, mock_get_json):
        """Test that public_repos returns the correct list of repository
        names"""

        # Example payload returned by get_json
        example_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl-3.0"}},
        ]

        # Expected repo names from the payload
        expected_repos = ["repo1", "repo2", "repo3"]

        # Set up the mocks
        mock_get_json.return_value = example_repos_payload
        mock_pub_rep_url.return_value = "https://fake.url/repos"

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the public_repos method
        repos = client.public_repos()

        # Assert the returned repo list is as expected
        self.assertEqual(repos, expected_repos)

        # Assert _public_repos_url was called once
        mock_pub_rep_url.assert_called_once()

        # Assert get_json was called once with the fake URL
        mock_get_json.assert_called_once_with("https://fake.url/repos")

    @patch("client.get_json")
    @patch.object(GithubOrgClient, "_public_repos_url",
                  new_callable=PropertyMock)
    def test_public_repos_with_license(self, mock_pub_rep_url, mock_get_json):
        """Test public_repos with a license filter."""

        # Example payload returned by get_json
        example_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl-3.0"}},
        ]

        # Expected repo names with apache-2.0 license
        expected_repos = ["repo2"]

        # Set up the mocks
        mock_get_json.return_value = example_repos_payload
        mock_pub_rep_url.return_value = "https://fake.url/repos"

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the public_repos method with license filter
        repos = client.public_repos(license="apache-2.0")

        # Assert the returned repo list is as expected
        self.assertEqual(repos, expected_repos)

        # Assert _public_repos_url was called once
        mock_pub_rep_url.assert_called_once()

        # Assert get_json was called once with the fake URL
        mock_get_json.assert_called_once_with("https://fake.url/repos")


if __name__ == "__main__":
    unittest.main()

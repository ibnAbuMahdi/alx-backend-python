#!/usr/bin/env python3
""" test client module """
from unittest import (TestCase, mock)
from unittest.mock import (patch, Mock)
from utils import (get_json, access_nested_map, memoize)
from client import (GithubOrgClient)
from typing import (Mapping, Sequence, Any)
from parameterized import (parameterized, parameterized_class)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """ test github org client class """
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @mock.patch('client.get_json')
    def test_org(self, name: str, mC: mock.Mock) -> None:
        """ tests the org method """
        url: str = "https://api.github.com/orgs/{org}"
        mC.return_value = {"payload": True}
        clnt: GithubOrgClient = GithubOrgClient(name)
        self.assertEqual(clnt.org, {"payload": True})
        mC.assert_called_once_with(url.format(org=name))

    def test_public_repos_url(self) -> None:
        """ test the method _public_repos_url """
        with mock.patch("client.GithubOrgClient.org",
                        new_callable=mock.PropertyMock,
                        return_value={"repos_url": "http://some.url"}) as mm:
            gc = GithubOrgClient("google")
            self.assertEqual(gc._public_repos_url, "http://some.url")

    @patch('client.get_json', return_value=[{"name": "A"}, {"name": "B"}])
    def test_public_repos(self, mjson: mock.Mock) -> None:
        """ tests public repos and more patching """
        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=mock.PropertyMock,
                        return_value="http://some.url") as mr:
            clnt: GithubOrgClient = GithubOrgClient('google')
            pr: List[str] = clnt.public_repos()
            self.assertEqual(pr, ["A", "B"])
            mr.assert_called_once()
            mjson.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo: Mapping, lkey: str, expd: bool) -> None:
        """ test the has license method """
        self.assertEqual(GithubOrgClient.has_license(repo, lkey), expd)


@parameterized_class([{"PAYLOAD": TEST_PAYLOAD}])
class TestIntegrationGithubOrgClient(TestCase):
    """ class for integration testing """

    @classmethod
    def setUpClass(cls):
        """ the setup class method """
        cls.get_patcher = patch('requests.get', side_effect=s_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ the tear down class method """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """ tests for public repos method """
        gc: GithubOrgClient = GithubOrgClient('google')
        self.assertEqual(gc.public_repos(), self.PAYLOAD[0][2])

    def test_public_repos_with_license(self) -> None:
        """ tests public repos with license """
        gc: GithubOrgClient = GithubOrgClient('google')
        self.assertEqual(gc.public_repos("apache-2.0"), self.PAYLOAD[0][3])


def s_effect(url: str) -> Any:
    """ side effect function """
    repos_url = "https://api.github.com/orgs/google/repos"
    org_url = "https://api.github.com/orgs/google"
    if url == repos_url:
        return Mock(json=Mock(return_value=TEST_PAYLOAD[0][1]))
    elif url == org_url:
        return Mock(json=Mock(return_value=TEST_PAYLOAD[0][0]))

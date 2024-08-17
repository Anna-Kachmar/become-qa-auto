import pytest
import requests

from Providers.Data.user_provider import UserProvider


def test_http_status_code200():
    r = requests.get('https://api.github.com/zen')
    # print(r.__dict__)
    assert r.status_code == 200
    # assert r.text != 'Anything added dilutes everything else.'

def test_user_exists(github_api_client):
    name = UserProvider.existing_user()

    user = github_api_client.get_user(name['username'])
    # print(r.__dict__)

    assert user['login'] == name['username']
    assert user['id'] == name['id']

def test_user_not_exists(github_api_client):
    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user('dgdgdrehetht')

    # print(r.__dict__)
    # assert user.status_code == 404
    # assert user['message'] == 'Not Found'
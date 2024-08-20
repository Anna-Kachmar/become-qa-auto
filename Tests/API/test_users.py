import pytest
import requests

from Providers.Data.user_provider import UsersProvider


def test_http_status_code200():
    r = requests.get('https://api.github.com/zen')
    # print(r.__dict__)
    assert r.status_code == 200

def test_user_exists(github_api_client):
    user = UsersProvider.existing_user()
    api_user = github_api_client.get_user(user['login'])
    # print(r.__dict__)

    assert api_user['login'] == user['login']
    assert api_user['id'] == user['id']

def test_user_not_exists(github_api_client):
    user = UsersProvider.fake_user()

    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user(user['login'])

    # print(r.__dict__)
    # assert user.status_code == 404
    # assert user['message'] == 'Not Found'
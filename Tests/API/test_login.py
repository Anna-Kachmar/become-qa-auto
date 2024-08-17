import pytest
import requests

def test_http_status_code200():
    r = requests.get('https://api.github.com/zen')
    # print(r.__dict__)
    assert r.status_code == 200
    # assert r.text != 'Anything added dilutes everything else.'

def test_user_exists(github_api_client):
    user = github_api_client.get_user('defunkt')
    # print(r.__dict__)

    assert user['login'] == 'defunkt'
    assert user['id'] == 2

def test_user_not_exists(github_api_client):
    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user('dgdgdrehetht')

    # print(r.__dict__)
    # assert user.status_code == 404
    # assert user['message'] == 'Not Found'
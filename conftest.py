import pytest
from Config.config import Config
from Applications.api.github_api import GitHubApi

@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubApi(Config.base_url)
    # return github_api_client
    yield github_api_client

    print('END-UP TEST')

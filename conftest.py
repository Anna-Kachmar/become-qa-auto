import pytest
from Applications.ui.github_ui import GitHubUI
from Config.config import Config
from Applications.api.github_api import GitHubApi
from selenium import webdriver


@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubApi(Config.base_url)
    # return github_api_client
    yield github_api_client

    print('END-UP TEST')

@pytest.fixture(scope='session')
def github_ui_client():
    # 1:
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 2:
    driver = webdriver.Chrome()
    github_ui_client = GitHubUI(Config.base_url_ui, driver)
    # return github_ui_client
    yield github_ui_client

    github_ui_client.close_browser()
    # driver.close()

from conftest import github_api_client
from Providers.Data.repositories_provider import RepositoriesProvider


def test_check_repos_can_be_found(github_api_client):
    #Check user can find existing repo from github
    repo = RepositoriesProvider.existing_repository()
    repos = github_api_client.get_repos(repo['name'])

    assert repos['total_count'] >= repo['total_count']

def test_check_repos_can_not_be_found(github_api_client):
    #Check user can find existing repo from github
    repo = RepositoriesProvider.non_existing_repository()
    repos = github_api_client.get_repos(repo['name'])
    # print(repos)

    assert repos['total_count'] == repo['total_count']

def test_check_total_count_eq_items_length_for_can_be_found(github_api_client):
    #Check user can find existing repo from github
    repo = RepositoriesProvider.existing_repository()
    repos = github_api_client.get_repos(repo['name'])

    assert len(repos['items']) >= repo['items_count']


def test_check_total_count_eq_items_length_for_not_be_found(github_api_client):
    #Check user can find existing repo from github
    repo = RepositoriesProvider.non_existing_repository()
    repos = github_api_client.get_repos(repo['name'])

    assert len(repos['items']) == repo['items_count']

# def test_check_repos_can_not_be_found(github_api_client):
#     #Check user can find existing repo from github
#     repos = github_api_client.get_repos('sjkncakjcnksjcnksajcnj')
#     # print(repos)
#
#     assert repos['total_count'] == 0
#     assert len(repos['items']) == 0

 # python3 -m pytest -s

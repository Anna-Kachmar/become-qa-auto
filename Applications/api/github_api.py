import requests
from apport.packaging_impl import HTTPError


class GitHubApi:

    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        r.raise_for_status()
        # if r.status_code != 200:
        #     raise HTTPError

        return r.json()

    def get_repos(self, repos_search_param: str):
        r = requests.get(
            f'https://api.github.com/search/repositories',
            # f'{self.base_url}/search/repositories?q={repos_search_param}',
            params={'q': repos_search_param},
        )
        r.raise_for_status()

        return r.json()

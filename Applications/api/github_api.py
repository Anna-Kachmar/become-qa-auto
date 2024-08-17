import requests
from apport.packaging_impl import HTTPError


class GitHubApi:

    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def get_user(self, username: str):
        r = requests.get(f'{self.base_url}/users/{username}')
        r.raise_for_status()
        # if r.status_code != 200:
        #     raise HTTPError

        return r.json()
        # return r

    def get_repos(self, repos_search_param: str):
        r = requests.get(
            f'{self.base_url}/search/repositories',
            # f'{self.base_url}/search/repositories?q={repos_search_param}',
            params={'q': repos_search_param},
        )
        r.raise_for_status()

        return r.json()

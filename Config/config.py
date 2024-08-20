import os


class Config:
    # base_url = 'https://api.github.com'
    base_url = os.environ.get('BASE_URL_API', 'https://api.github.com'),
    base_url_ui = 'https://github.com'

    # BASE_URL = 'https://api.github.com' python3 - m pytest - s
    # export EXISTING_GITHUB_USER_LOGIN='defunkt'
    # echo $EXISTING_GITHUB_USER_ID
    # unset  EXISTING_GITHUB_USER_ID
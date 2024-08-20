import os

class UsersProvider:

    @staticmethod
    def fake_user():
        return {
            'login': 'some_name',
            'id': '464664'
        }

    @staticmethod
    def existing_user():
        return {
            'login': 'defunkt',
            'id': 2,
            'password': 'password'
        }

    @staticmethod
    def existing_user_from_env():
        return {
            'login': os.environ.get("EXISTING_GITHUB_USER_LOGIN"),
            'id': int(os.environ.get("EXISTING_GITHUB_USER_ID")),
        }


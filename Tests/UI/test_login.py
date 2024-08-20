from Providers.Data.user_provider import UsersProvider


def test_check_login_failed(github_ui_client):
    user = UsersProvider.existing_user()

    github_ui_client.login(user['login'], user['password'])

    assert  github_ui_client.get_title() == "Sign in to GitHub · GitHub"

    # driver.close()

    # python3 - m pytest - k test_check_login
    # pytest - k test_check_login
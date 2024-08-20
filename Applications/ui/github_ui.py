from Config.config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GitHubUI:

    def __init__(self, base_url, driver):
        self.base_url = base_url
        self.driver = driver

    def login(self, username, user_password):
        # name of fixture using here
        self.driver.get(f'{Config.base_url_ui}/login')

        elem = self.driver.find_element(By.ID, "login_field")
        elem.send_keys(username)

        elem = self.driver.find_element(By.ID, "password")
        elem.send_keys(user_password)

        elem.send_keys(Keys.RETURN)

        return True
    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title

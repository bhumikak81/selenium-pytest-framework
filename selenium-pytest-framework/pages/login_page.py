from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self, base_url):
        self.go_to(base_url)

    def login(self, username, password):
        self.type(*self.USERNAME, text=username)
        self.type(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BTN)

    def error_message(self):
        return self.text_of(*self.ERROR_MSG)

from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def start_checkout(self):
        self.click(*self.CHECKOUT_BTN)

    def fill_information(self, first, last, postal):
        self.type(*self.FIRST_NAME, text=first)
        self.type(*self.LAST_NAME, text=last)
        self.type(*self.POSTAL_CODE, text=postal)
        self.click(*self.CONTINUE_BTN)

    def finish(self):
        self.click(*self.FINISH_BTN)

    def success_message(self):
        return self.text_of(*self.COMPLETE_HEADER)

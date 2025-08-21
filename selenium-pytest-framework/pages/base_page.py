from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def go_to(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        self.wait.until(EC.element_to_be_clickable((by, locator))).click()

    def type(self, by, locator, text, clear=True):
        el = self.wait.until(EC.visibility_of_element_located((by, locator)))
        if clear:
            el.clear()
        el.send_keys(text)

    def visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def text_of(self, by, locator):
        return self.visible(by, locator).text

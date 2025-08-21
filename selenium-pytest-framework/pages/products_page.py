from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    FIRST_ADD_TO_CART = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def is_loaded(self):
        self.visible(*self.INVENTORY_CONTAINER)
        return True

    def add_first_item_to_cart(self):
        self.click(*self.FIRST_ADD_TO_CART)

    def cart_count(self):
        # Returns badge text or "0" if no badge
        badges = self.finds(*self.CART_BADGE)
        return badges[0].text if badges else "0"

    def go_to_cart(self):
        self.click(*self.CART_LINK)

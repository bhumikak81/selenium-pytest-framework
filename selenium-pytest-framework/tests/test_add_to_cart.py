from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_item_to_cart(driver, config):
    base = config["base_url"]
    creds = config["credentials"]

    lp = LoginPage(driver)
    lp.open(base)
    lp.login(creds["valid_username"], creds["valid_password"])

    pp = ProductsPage(driver)
    assert pp.is_loaded()

    pp.add_first_item_to_cart()
    assert pp.cart_count() == "1"

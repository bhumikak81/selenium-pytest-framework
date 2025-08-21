from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver, config):
    base = config["base_url"]
    creds = config["credentials"]

    # Login
    lp = LoginPage(driver)
    lp.open(base)
    lp.login(creds["valid_username"], creds["valid_password"])

    # Add to cart
    pp = ProductsPage(driver)
    assert pp.is_loaded()
    pp.add_first_item_to_cart()
    pp.go_to_cart()

    # Checkout
    co = CheckoutPage(driver)
    co.start_checkout()
    co.fill_information("Bhumika", "K", "403001")
    co.finish()

    assert "Thank you for your order" in co.success_message()

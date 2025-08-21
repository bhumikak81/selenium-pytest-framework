import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_valid_login(driver, config):
    lp = LoginPage(driver)
    base = config["base_url"]
    creds = config["credentials"]

    lp.open(base)
    lp.login(creds["valid_username"], creds["valid_password"])

    pp = ProductsPage(driver)
    assert pp.is_loaded()

def test_invalid_login(driver, config):
    lp = LoginPage(driver)
    base = config["base_url"]
    creds = config["credentials"]

    lp.open(base)
    lp.login(creds["invalid_username"], creds["invalid_password"])

    msg = lp.error_message()
    assert "Epic sadface" in msg or "locked out" in msg.lower()

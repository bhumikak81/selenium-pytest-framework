## Selenium + Pytest Automation Framework (SauceDemo)
This is a Python Selenium automation framework built using Pytest and Page Object Model (POM).It automates end-to-end test flows on SauceDemo, including login, add to cart, and checkout

## Features
Page Object Model (POM) → clean & reusable code
Cross-Browser Support → Chrome & Firefox (configurable)
Config Driven → manage browser, URL, credentials in config.json
Pytest Fixtures → WebDriver setup/teardown in conftest.py
Reports → generates detailed pytest-html reports

## Scenarios Covered:
Valid login
Invalid login
Add product to cart
Checkout flow

## Project Structure
selenium-pytest-framework/
├── tests/
│   ├── test_login.py          # Login tests (valid/invalid)
│   ├── test_add_to_cart.py    # Add to cart test
│   └── test_checkout.py       # Checkout flow
├── pages/
│   ├── base_page.py           # Common Selenium actions
│   ├── login_page.py          # Login page actions
│   ├── products_page.py       # Product/cart actions
│   └── checkout_page.py       # Checkout process
├── config/
│   └── config.json            # URL, browser, credentials
├── reports/                   # HTML reports stored here
├── conftest.py                # Pytest fixtures for WebDriver
├── pytest.ini                 # Pytest settings
├── requirements.txt           # Dependencies
└── README.md                  # Instructions

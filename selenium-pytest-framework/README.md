# Selenium + Pytest Automation Framework (SauceDemo)

A ready-to-run Selenium automation framework using Pytest and Page Object Model. 
It covers login, add-to-cart, and checkout flows on https://www.saucedemo.com/.

## Quick Start

1. Create a virtual environment (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests with HTML report
   ```bash
   pytest --html=reports/report.html
   ```

4. Change settings in `config/config.json` (browser: chrome/firefox, headless: true/false).

## Project Structure
```
selenium-pytest-framework/
├── tests/
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   └── test_checkout.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── checkout_page.py
├── config/
│   └── config.json
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Notes
- Uses `webdriver-manager` to auto-manage browser drivers.
- Default credentials are for SauceDemo's public test account.
- If running headless on CI, set `"headless": true` in `config/config.json`.

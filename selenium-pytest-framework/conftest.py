import json
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="session")
def config():
    cfg_path = os.path.join(os.path.dirname(__file__), "config", "config.json")
    with open(cfg_path, "r") as f:
        return json.load(f)

@pytest.fixture
def driver(config):
    browser = config.get("browser", "chrome").lower()
    headless = config.get("headless", False)
    implicit_wait = int(config.get("implicit_wait", 5))

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        service = ChromeService(ChromeDriverManager().install())
        drv = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        service = FirefoxService(GeckoDriverManager().install())
        drv = webdriver.Firefox(service=service, options=options)
        try:
            drv.maximize_window()
        except Exception:
            pass
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    drv.implicitly_wait(implicit_wait)
    yield drv
    drv.quit()

import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_driver():
    driver_options = webdriver.FirefoxOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options
    browser.config.base_url = "https://demoqa.com"
    yield
    browser.quit()

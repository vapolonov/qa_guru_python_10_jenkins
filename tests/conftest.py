import pytest
from selene.support.shared import browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

# DEFAULT_BROWSER_VERSION = "100.0"


# @pytest.fixture(scope='function', autouse=True)
# def browser_management():
#     browser.config.base_url = 'https://demoqa.com'
#     browser.config.browser_name = 'chrome'
#     browser.config.timeout = 3
#     browser.config.window_width = 1920
#     browser.config.window_height = 1920

@pytest.fixture(scope='function')
def setup_chrome():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1090
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    # browser = Browser(Config(driver))

    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

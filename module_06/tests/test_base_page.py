from common.webdriver_factory import get_driver
from module_06.src.pages.base_page import BasePage


def test_base_page():
    driver = get_driver('chrome')
    page = BasePage(driver, 'https://www.google.com')
    page.open()
    page.wait_until_loaded()
    page.timeout = 10
    assert page.timeout == 10, 'Page timeout should be 10'
    page.close()

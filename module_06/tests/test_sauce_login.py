"""Sauce lab login tests."""
from common.webdriver_factory import get_driver
from module_06.src.pages.login import LoginPage


def test_sauce_lab_login():
    driver = get_driver('chrome')
    page = LoginPage(driver)
    page.open()
    page.login('standard_user', 'secret_sauce')
    page.close()

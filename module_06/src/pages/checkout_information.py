"""Implements sauce lab login inventory."""
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.elements.header import Header
from module_06.src.locators.checkout_step1 import CheckInfo
from module_06.src.pages.base_page import BasePage


_URL = 'https://www.saucedemo.com/checkout-step-one.html'


class CheckoutInformation(BasePage):
    """Sauce lab login."""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self._first_name = BasePageElement(CheckInfo.FIRST_NAME, wait=self._wait)
        self._last_name = BasePageElement(CheckInfo.LAST_NAME, wait=self._wait)
        self._zip_code = BasePageElement(CheckInfo.ZIP_CODE, wait=self._wait)
        self._continue_btn = BasePageElement(CheckInfo.CONTINUE_BTN, wait=self._wait)
        self._cancel_btn = BasePageElement(CheckInfo.CANCEL_BTN, wait=self._wait)

    def click_checkout_cancel(self):
        self._cancel_btn.click()

    def click_checkout_continue(self):
        self._continue_btn.click()

"""Implements sauce lab login inventory."""
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.elements.header import Header
from module_06.src.locators.checkout import CartLoc
from module_06.src.pages.base_page import BasePage


_URL = 'https://www.saucedemo.com/cart.html'


class CheckoutPage(BasePage):
    """Sauce lab login."""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self._continue_shopping_btn = BasePageElement(CartLoc.CONTINUE_SHOPPING_BTN, wait=self._wait)
        self._checkout_btn = BasePageElement(CartLoc.CHECKOUT_BTN, wait=self._wait)

    def click_checkout(self):
        self._checkout_btn.click()

    def click_continue_shopping(self):
        self._continue_shopping_btn.click()

"""Abstraction to interact with inventory items."""
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.header import HeaderLoc



class Header:
    """Represents inventory item."""

    def __init__(self, wait: WebDriverWait):
        self._wait = wait
        self._link = BasePageElement(HeaderLoc.LINK, wait=wait)
        self._badge = BasePageElement(HeaderLoc.BADGE, wait=wait)
        self._burger_btn = BasePageElement(HeaderLoc.BURGER_BTN, wait=wait)

    def get_total_cart_items(self) -> int:
        """Get total items in cart"""
        try:
            return int(self._badge.get_text())
        except Exception:
            return 0

    def goto_cart(self):
        """Go to cart."""
        self._link.click()


    def open_menu(self):
        """Open menu"""
        self._burger_btn.click()

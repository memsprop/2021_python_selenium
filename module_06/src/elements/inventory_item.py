"""Abstraction to interact with inventory items."""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.inventory_item import InventoryItemLoc
from module_06.src.mixin.inventoryItemMixin import InventoryItemMixin
from module_06.src.pages.inventory_details import InventoryDetailsPage


class InventoryItem(InventoryItemMixin):
    """Represents inventory item."""

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self._title = BasePageElement(InventoryItemLoc.TITLE, wait=wait, root=root)
        self._description = BasePageElement(InventoryItemLoc.DESCRIPTION, wait=wait, root=root)
        self._price = BasePageElement(InventoryItemLoc.PRICE, wait=wait, root=root)
        self._inv_btn = BasePageElement(InventoryItemLoc.BTN, wait=wait, root=root)

    def open_details(self):
        """Open product details"""
        self._title.click()
        return InventoryDetailsPage(self._wait._driver, self._wait._timeout)

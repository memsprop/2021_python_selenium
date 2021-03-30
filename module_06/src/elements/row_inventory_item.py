"""Abstraction to interact with inventory items."""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.checkout import CartLoc
from module_06.src.locators.inventory_item import InventoryItemLoc
from module_06.src.mixin.inventoryItemMixin import InventoryItemMixin


class RowInventoryItem(InventoryItemMixin):
    """Represents inventory item."""

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self._title = BasePageElement(InventoryItemLoc.TITLE, wait=wait)
        self._description = BasePageElement(InventoryItemLoc.DESCRIPTION, wait=wait)
        self._price = BasePageElement(InventoryItemLoc.PRICE, wait=wait)
        self._inv_btn = BasePageElement(InventoryItemLoc.BTN, wait=waint)

    def get_qty(self):
        return 0

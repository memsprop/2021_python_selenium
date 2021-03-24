
"""Inventory page locators."""
from selenium.webdriver.common.by import By


class InventoryPageLoc:
    """Inventory page locators."""
    ITEMS = (By.CLASS_NAME, 'inventory_item')
    LABEL = (By.CLASS_NAME, 'product_label')
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
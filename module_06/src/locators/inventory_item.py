"""Locators for inventory items"""
from selenium.webdriver.common.by import By


class InventoryItemLoc:
    """Inventory item locators.
    Locators are relative to parent container div.
    """
    TITLE = (By.CLASS_NAME, 'inventory_item_name')
    DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    PRICE = (By.CLASS_NAME, 'inventory_item_price')
    BTN = (By.XPATH, ".//button[contains(@class,'btn_inventory')]")

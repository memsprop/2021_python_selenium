"""Locators for inventory details items"""
from selenium.webdriver.common.by import By


class InventoryDetailsLoc:
    """Inventory item locators.
    Locators are relative to parent container div.
    """
    TITLE = (By.CLASS_NAME, 'inventory_details_name')
    DESCRIPTION = (By.CLASS_NAME, 'inventory_details_desc')
    PRICE = (By.CLASS_NAME, 'inventory_details_price')
    BTN = (By.XPATH, "//button[contains(@class,'btn_inventory')]")
    BACK_BTN = (By.CLASS_NAME, 'inventory_details_back_button')
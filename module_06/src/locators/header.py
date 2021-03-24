"""Locators for inventory details items"""
from selenium.webdriver.common.by import By


class HeaderLoc:
    """Inventory item locators.
    Locators are relative to parent container div.
    """
    BADGE = (By.XPATH, "//span[contains(@class,'shopping_cart_badge')]")
    LINK = (By.XPATH, "//a[contains(@class,'shopping_cart_link')]")
    BURGER_BTN = (By.CLASS_NAME, 'bm-burger-button')

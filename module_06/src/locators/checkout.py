"""Locators for Your Cart items"""
from selenium.webdriver.common.by import By


class CartLoc:
    """Cart item locators.
    Locators are relative to parent container div.
    """

    CART_LST = (By.CLASS_NAME, 'cart_list')
    CHECKOUT_BTN = (By.CLASS_NAME, 'btn_action checkout_button')
    CONTINUE_SHOPPING_BTN = (By.CLASS_NAME, 'btn_secondary')

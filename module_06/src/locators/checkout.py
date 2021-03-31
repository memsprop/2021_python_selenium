"""Locators for Your Cart items"""
from selenium.webdriver.common.by import By


class CartLoc:
    """Cart item locators.
    Locators are relative to parent container div.
    """

    CART_LST = (By.CLASS_NAME, 'cart_list')
    CHECKOUT_BTN = (By.XPATH, "//*[@class='cart_footer']/a[contains(@class,'btn_action')]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//*[@class='cart_footer']/a[contains(@class,'btn_secondary')]")




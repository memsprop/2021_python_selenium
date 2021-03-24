
from module_06.src.elements.inventory_item import InventoryItem
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.inventory_details import InventoryDetailsLoc


class InventoryDetails(InventoryItem):

    def __init__(self, wait: WebDriverWait):
        self.__title = BasePageElement(InventoryDetailsLoc.TITLE, wait=wait)
        self.__description = BasePageElement(InventoryDetailsLoc.DESCRIPTION, wait=wait)
        self.__price = BasePageElement(InventoryDetailsLoc.PRICE, wait=wait)
        self.__inv_btn = BasePageElement(InventoryDetailsLoc.BTN, wait=wait)
        self.__back_btn = BasePageElement(InventoryDetailsLoc.BACK_BTN, wait=wait)

    def go_back(self):
        """Open product details"""
        self.__back_btn.click()

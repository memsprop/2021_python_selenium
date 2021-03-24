"""Includes function to control sauce lab inventory page."""
from collections import namedtuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

InventoryItem = namedtuple('InventoryItem', ['title', 'description', 'price'])


def get_inventory(wait: WebDriverWait) -> list:
    """Get inventory items.
    :param wait: Instance of web driver wait
    :return: List with product information.
    """
    items_loc = (By.CLASS_NAME, 'inventory_item')
    elements = wait.until(EC.visibility_of_all_elements_located(items_loc))
    result = []
    for index, element in enumerate(elements):
        element: WebElement
        title = element.find_element_by_class_name('inventory_item_name').text
        description = element.find_element_by_class_name('inventory_item_desc').text
        price = element.find_element_by_class_name('inventory_item_price').text
        tmp = InventoryItem(title, description, price)
        result.append(tmp)
    return result

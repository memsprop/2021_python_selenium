"""Test cases for inventory"""
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from module_05.sauce_func_lib.inventory import get_inventory, InventoryItem
from module_05.sauce_func_lib.login import login


VALID_PRICES = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']

LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
]


@pytest.mark.parametrize('user, password', LOGIN_DATA)
def test_inventory_size(user: str, password: str):
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 3)
    driver.get('https://www.saucedemo.com/')
    login(wait, user, password)
    items = get_inventory(wait)
    assert len(items) == 6, 'Inventory should contain 6 items'
    driver.close()


def test_inventory_prices():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    for index, item in enumerate(items):
        item: InventoryItem
        assert item.price == VALID_PRICES[index], f'Price for item {index} should be {VALID_PRICES[index]}'
    driver.close()

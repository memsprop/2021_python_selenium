"""Test cases for inventory item"""
from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.inventory import InventorySortOptions
from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase


_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

VALID_PRICES = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']
PRICES_LOW_HIGH = ['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99']
PRICES_HIGH_LOW = ['$49.99', '$29.99', '$15.99', '$15.99', '$9.99', '$7.99']

class TestInventory(TestBase):

    def test_prices(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for index, item in enumerate(inventory.products):
            item: InventoryItem
            assert item.get_price() == VALID_PRICES[index], f'Price for item {index} should be {VALID_PRICES[index]}'
            print('\n')
            print(item.get_title())
            print(item.get_description())
            print(item.get_price())
            print('*' * 80)

    def test_label(self):
        """Test production label."""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        assert inventory.get_label() == 'Products', 'Inventory page label should be Products'

    def test_sort(self):
        """Test sort products"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.get_sort_value() == InventorySortOptions.A_TO_Z.value, 'Default sort should be A to Z'
        for option in InventorySortOptions:
            inventory.sort_by(option)
            inventory.get_sort_value() == option.value, f'Default sort should be {option.value}'

    def test_sort_price_lh(self):
        """Test sort products"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.get_sort_value() == InventorySortOptions.A_TO_Z, 'Default sort should be A to Z'
        inventory.sort_by(InventorySortOptions.PRICE_LOW_TO_HIGH)
        for index, item in enumerate(inventory.products):
            item: InventoryItem
            assert item.get_price() == PRICES_LOW_HIGH[index], f'Price for item {index} should be {VALID_PRICES[index]}'
            print('\n')
            print(item.get_title())
            print(item.get_description())
            print(item.get_price())
            print('*' * 80)

    def test_sort_price_hl(self):
        """Test sort products"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.get_sort_value() == InventorySortOptions.A_TO_Z, 'Default sort should be A to Z'
        inventory.sort_by(InventorySortOptions.PRICE_HIGH_TO_LOW)
        for index, item in enumerate(inventory.products):
            item: InventoryItem
            assert item.get_price() == PRICES_HIGH_LOW[index], f'Price for item {index} should be {VALID_PRICES[index]}'
            print('\n')
            print(item.get_title())
            print(item.get_description())
            print(item.get_price())
            print('*' * 80)

    def test_sort_price_za(self):
        """Test sort products"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.get_sort_value() == InventorySortOptions.A_TO_Z, 'Default sort should be A to Z'
        inventory.sort_by(InventorySortOptions.Z_TO_A)
        prods = [] #empty list where with the following for I got the
        # List of all products sorted by name from z to a
        for index, item in enumerate(inventory.products):
            item: InventoryItem
            prods.append(item.get_title())

        for index, item in enumerate(inventory.products):
            item: InventoryItem
            assert item.get_title() == prods[index], f'Price for item {index} should be {VALID_PRICES[index]}'
            print('\n')
            print(item.get_title())
            print(item.get_description())
            print(item.get_price())
            print('*' * 80)
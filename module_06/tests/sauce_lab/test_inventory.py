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
        assert inventory.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

    def test_sort(self):
        """Test sort products"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.get_sort_value() == InventorySortOptions.A_TO_Z.value, 'Default sort should be A to Z'
        for option in InventorySortOptions:
            inventory.sort_by(option)
            inventory.get_sort_value() == option.value, f'Default sort should be {option.value}'

    def test_add_and_remove_two_items(self):
        """Test adding and removing items from main page"""
        login = LoginPage(self.driver) #SAUCE-LAB-5
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        print('\n')
        print(first_item.get_title())
        print(first_item.get_description())
        print(first_item.get_price())
        print('*' * 80)
        second_item = inventory_page.products[4]
        second_item: InventoryItem
        second_item.add_to_cart()
        print('\n')
        print(second_item.get_title())
        print(second_item.get_description())
        print(second_item.get_price())
        print('*' * 80)
        first_item.remove_from_cart()
        second_item.remove_from_cart()
        print(f'Products {first_item.get_title()} and {second_item.get_title()} were successfully removed')

    def test_add_all(self): #SAUCE-LAB-7
        """Test add to cart all item"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products
        first_item: InventoryItem
        for item in first_item:
            item.add_to_cart()
        if inventory_page.header.get_total_cart_items() == 6:
            print('\n')
            print(f'Total of products {inventory_page.header.get_total_cart_items()}')
        else:
            print('\n')
            print('Not all items were added')

    def test_remove_all(self): #SAUCE-LAB-8
        """Test add to cart all item"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products
        first_item: InventoryItem
        for item in first_item:
            item.add_to_cart()
        if inventory_page.header.get_total_cart_items() == 6:
            print('\n')
            print(f'Total of products {inventory_page.header.get_total_cart_items()}')
        else:
            print('Not all items were added')
        for item in first_item:
            item.remove_from_cart()
        if inventory_page.header.get_total_cart_items() == 0:
            print('\n')
            print(f'Total of products {inventory_page.header.get_total_cart_items()}')
        else:
            print('Not all items were removed')

    def test_sort_price_lh(self): #SAUCE-LAB-9
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

    def test_sort_price_hl(self): #SAUCE-LAB-10
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

    def test_sort_price_za(self): #SAUCE-LAB-11
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


"""Test cases for inventory item"""
from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.inventory import InventorySortOptions
from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase


_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'


class TestInventoryDetails(TestBase):

    def test_inventory_details(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        print(f'Title: {details_page.get_title()}')
        print(f'Description: {details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')
        details_page.add_to_cart()
        print(f'Total elements in cart: {details_page.header.get_total_cart_items()}')
        details_page.remove_from_cart()
        details_page.back()
        inventory_page.products.reload()
        assert len(inventory_page.products) == 6, 'Inventor len should be 6'

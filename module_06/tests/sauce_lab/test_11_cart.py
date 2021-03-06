"""Test cases for inventory item"""
from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.checkout import CheckoutPage
from module_06.src.pages.checkout_information import CheckoutInformation
from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

VALID_PRICES = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']

class TestCart(TestBase):

    def test_checkout_continue_shopping(self): #SAUCE-LAB-12
        """Test add to cart first item"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        print(f'Total of products {inventory_page.header.get_total_cart_items()}')
        inventory_page.header.goto_cart()
        checkout_item = CheckoutPage(self.driver, 5)
        checkout_item.click_continue_shopping()
        inventory_page.products.reload()
        assert len(inventory_page.products) == 6, 'Inventor len should be 6'

    def test_cancel_checkout_item(self): #SAUCE-LAB-13
        """Test add to cart first item"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        print(f'Total of products {inventory_page.header.get_total_cart_items()}')
        inventory_page.header.goto_cart()
        checkout_item = CheckoutPage(self.driver, 5)
        checkout_item.click_checkout()
        checkout_page = CheckoutInformation(self.driver, 5)
        checkout_page.click_checkout_cancel()


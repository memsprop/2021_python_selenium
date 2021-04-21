"""Sauce login tests."""
import pytest
from module_06.src.pages.login import LoginPage
from module_06.tests.common.test_base import TestBase


LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
]

_DEF_USER = 'standard_user'
_DEF_PASSWORD = 'secret_sauce'

ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'
ERROR_LOCKED = 'Epic sadface: Sorry, this user has been locked out.'

class TestLogin(TestBase):

    @pytest.mark.sanity
    @pytest.mark.login
    @pytest.mark.parametrize('user, password', LOGIN_DATA)
    def test_valid_user(self, user: str, password: str):
        """SAUCE-LAB-1"""
        page = LoginPage(self.driver)
        page.open()
        page.login(user, password)

    @pytest.mark.regression
    @pytest.mark.login
    def test_invalid_user(self):
        """SAUCE-LAB-2"""
        page = LoginPage(self.driver)
        page.open()
        page.login('standard_user', 'invalid_password')
        error_msg = page.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == ERROR_MSG, f'Error message should be {ERROR_MSG}'


    def test_login_logout(self):
        """SAUCE-LAB-3"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory_page.header.open_menu()
        inventory_page.header.logout()
        print('\n')
        print('LOGOUT Successfully')

    def test_locked_user(self):
        """SAUCE-LAB-4 Locked user"""
        page = LoginPage(self.driver)
        page.open()
        page.login('locked_out_user', 'secret_sauce')
        error_msg = page.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for locked user'
        assert error_msg == ERROR_LOCKED, f'Error message should be {ERROR_LOCKED}'

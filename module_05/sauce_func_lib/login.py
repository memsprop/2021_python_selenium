"""Includes Function to control saocu lab login page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from module_05.sauce_func_lib.common import write_to_input, click, get_text


def login(wait: WebDriverWait, user: str, password: str):
    """Login to sauce lab

    :param wait: Instance of web driver wait.
    :param user: User email
    :param password: User password
    :return: None
    """
    user_locator = (By.ID, 'user-name')
    write_to_input(wait, user_locator, user)
    pass_locator = (By.ID, 'password')
    write_to_input(wait, pass_locator, password)
    login_locator = (By.ID, 'login-button')
    click(wait, login_locator)


def get_login_error(wait: WebDriverWait):
    """Get login error message

    :param wait:
    :return:
    """
    #//*[@data-test='error']
    #//*[@class='error-button']
    #try catch
    #find elements => []
    locator = (By.XPATH, "//*[@data-test='error']")
    return get_text(wait, locator)
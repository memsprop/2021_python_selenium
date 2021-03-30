
"""Select element."""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement


class SelectElement(BasePageElement):
    """Represents any input text element."""
    def __init__(self, loc: tuple, wait: WebDriverWait = None, root: WebElement = None):
        super().__init__(loc, wait, root)

    def get_select_instance(self) -> Select:
        """Get instance of select."""
        element = self.wait_until_loaded()
        return Select(element)

    def select_by_value(self, option):
        """Select by value."""
        self.get_select_instance().select_by_value(option)

    def get_selected_value(self):
        """Get selected value."""
        self.get_select_instance().first_selected_option.get_attribute('value')
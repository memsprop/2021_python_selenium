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
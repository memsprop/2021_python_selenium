from selenium.webdriver.common.by import By


class CheckInfo:
    """Cart item locators.
    Locators are relative to parent container div.
    """

    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.XPATH, "//*[@class='checkout_buttons']/input[contains(@class,'cart_button)]")
    CANCEL_BTN = (By.XPATH, "//*[@class='checkout_buttons']/a[contains(@class,'cart_cancel_link')]")
